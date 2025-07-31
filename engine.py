import json
from urllib import response
import Nuvolo_Client as NC
import Claroty_Client as CC

cmms = NC.NuvoloClient()
xdome = CC.ClarotyClient()

matched_device_count = 0

import concurrent.futures

devices_cmms = cmms.search_devices(limit=300, u_scripps_bio_active="true")
devices_list = devices_cmms.json().get("result", [])

def process_device(device):
    beic = device.get('name')
    device_xdome = xdome.get_devices(filter_by={"cmdb_asset_tag": beic}, fields=["name", "ip_address"])
    if device_xdome.status_code == 200:
        if device_xdome:
            print(f"Device {beic} found in XDome")
            return 1
    return 0

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_device, devices_list))
    matched_device_count = sum(results)

print(f"Total matched devices: {matched_device_count}")