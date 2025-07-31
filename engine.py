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
) -> int:
    """Return the number of CMMS devices whose name matches a xDome asset tag."""
    devices_response = cmms_client.search_devices(limit=300, u_scripps_bio_active="true")
    devices = devices_response.json().get("result", [])

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
    args = parser.parse_args()

    cmms = NC.NuvoloClient()
    xdome = CC.ClarotyClient()
    count = find_matches(cmms, xdome, num_threads=args.threads)
    print(f"Total matched devices: {count}")
