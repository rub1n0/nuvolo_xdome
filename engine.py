import os
import argparse

from dotenv import load_dotenv
from nuvolo_xdome.clients import NuvoloCMMSClient

load_dotenv()

INSTANCE = os.getenv("INSTANCE", "scrippscmms")
USER = os.getenv("USER", "svc_xdome_rest")
PASSWORD = os.getenv(
    "PASSWORD",
    "Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC",
)
TABLE = os.getenv("TABLE", "x_nuvo_eam_clinical_devices")

client = NuvoloCMMSClient(f"https://{INSTANCE}.service-now.com", USER, PASSWORD)

def get_devices(client: NuvoloCMMSClient, table: str, limit: int = 20):
    return client.search_assets(table, sysparm_fields="sys_id,name", sysparm_limit=limit)

def print_devices(results):
    for record in results:
        print(f"sys_id: {record.get('sys_id')}, name: {record.get('name')}")

def update_ip_address(client: NuvoloCMMSClient, table: str, sys_id: str, ip_address: str):
    """Set the ip_address field for the given record."""
    result = client.update_asset(table, sys_id, {"ip_address": ip_address})
    print(f"Successfully updated ip_address to {ip_address} for sys_id {sys_id}")
    return result


def add_multiple_ips(client: NuvoloCMMSClient, table: str, sys_id: str, ip_list):
    """
    Adds multiple IPs to the ip_addresses field, each on a new line.
    """
    ip_addresses = "\n".join(ip_list)
    result = client.update_asset(table, sys_id, {"ip_addresses": ip_addresses})
    print(
        f"Successfully updated ip_addresses to:\n{ip_addresses}\nfor sys_id {sys_id}"
    )
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description="Update asset IP addresses")
    parser.add_argument("--sys-id", required=True, help="Sys_id of the asset")
    parser.add_argument(
        "--ip-address",
        help="Single IP address to set (mutually exclusive with --ip-list)",
    )
    parser.add_argument(
        "--ip-list",
        help="Comma separated list of IPs to set (mutually exclusive with --ip-address)",
    )
    args = parser.parse_args()

    if args.ip_list:
        ip_list = [ip.strip() for ip in args.ip_list.split(",") if ip.strip()]
        result = add_multiple_ips(client, TABLE, args.sys_id, ip_list)
    elif args.ip_address:
        result = update_ip_address(client, TABLE, args.sys_id, args.ip_address)
    else:
        parser.error("Either --ip-address or --ip-list is required")

    print(result)


if __name__ == '__main__':
    main()
