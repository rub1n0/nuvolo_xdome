import argparse
import concurrent.futures

from tqdm import tqdm

import Nuvolo_Client as NC
import Claroty_Client as CC


def find_matches(
    cmms_client: NC.NuvoloClient,
    xdome_client: CC.ClarotyClient,
    *,
    num_threads: int | None = None,
    limit: int = 300,
    device_filters: dict[str, str] | None = None,
) -> int:
    """Return the number of CMMS devices whose name matches a xDome asset tag."""

    devices: list[dict] = []
    remaining = limit
    offset = 0
    while remaining > 0:
        batch_size = min(remaining, 1000)
        filter_kwargs = device_filters or {}
        resp = cmms_client.search_devices(
            limit=batch_size,
            offset=offset,
            **filter_kwargs,
        )
        batch = resp.json().get("result", [])
        if not batch:
            break
        devices.extend(batch)
        offset += len(batch)
        remaining -= len(batch)
        if len(batch) < batch_size:
            break

    def lookup(device):
        name = device.get("name")
        if not name:
            return 0
        resp = xdome_client.get_devices(
            fields=["name", "ip_address", "cmdb_asset_tag"],
            filter_by={"cmdb_asset_tag": name},
            limit=1,
        )
        if resp.status_code != 200:
            return 0
        matches = resp.json().get("devices", [])
        if matches:
            print(f"Device {name} found in xDome")
            return 1
        return 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as exe:
        results = []
        for result in tqdm(
            exe.map(lookup, devices),
            total=len(devices),
            desc="Matching",
        ):
            results.append(result)
        return sum(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find CMMS/xDome device matches")
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=None,
        help="Number of worker threads to use",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=300,
        help="Maximum number of CMMS devices to process",
    )
    parser.add_argument(
        "-f",
        "--filter",
        action="append",
        default=[],
        metavar="FIELD=VALUE",
        help=(
            "Optional CMMS query filter in ServiceNow format. "
            "Can be provided multiple times."
        ),
    )
    args = parser.parse_args()

    filter_kwargs: dict[str, str] = {}
    for item in args.filter:
        if "=" not in item:
            parser.error(f"Invalid filter '{item}'. Expected format FIELD=VALUE.")
        key, value = item.split("=", 1)
        if not key:
            parser.error(f"Invalid filter '{item}'. Field name is required.")
        filter_kwargs[key] = value

    cmms = NC.NuvoloClient()
    xdome = CC.ClarotyClient()
    count = find_matches(
        cmms,
        xdome,
        num_threads=args.threads,
        limit=args.limit,
        device_filters=filter_kwargs or None,
    )
    print(f"Total matched devices: {count}")
