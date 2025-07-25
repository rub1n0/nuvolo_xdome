import os

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
ip_address = os.getenv("IP_ADDRESS", "192.168.1.1")
ip_list = [ip.strip() for ip in os.getenv("IP_LIST", "192.168.1.1,192.168.1.2,192.368.1.3").split(",")]
sys_id = os.getenv("SYS_ID", "fd7c101cebcb6e10b8ceff47bad0cd99")

client = NuvoloCMMSClient(f"https://{INSTANCE}.service-now.com", USER, PASSWORD)

def get_devices(client: NuvoloCMMSClient, table: str, limit: int = 20):
    return client.search_assets(table, sysparm_fields="sys_id,name", sysparm_limit=limit)

def print_devices(results):
    for record in results:
        print(f"sys_id: {record.get('sys_id')}, name: {record.get('name')}")

def update_ip_address(client: NuvoloCMMSClient, table: str, sys_id: str, ip_address: str):
    client.update_asset(table, sys_id, {"ip_address": ip_address})
    print(f"Successfully updated ip_addresses to {ip_address} for sys_id {sys_id}")

def add_multiple_ips(client: NuvoloCMMSClient, table: str, sys_id: str, ip_list):
    """
    Adds multiple IPs to the ip_addresses field, each on a new line.
    """
    ip_addresses = "\n".join(ip_list)
    client.update_asset(table, sys_id, {"ip_addresses": ip_addresses})
    print(f"Successfully updated ip_addresses to:\n{ip_addresses}\nfor sys_id {sys_id}")

def main():
    results = add_multiple_ips(client, TABLE, sys_id, ip_list)
    print(results)

if __name__ == '__main__':
    main()
