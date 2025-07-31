import json
from urllib import response
import Nuvolo_Client as NC
import Claroty_Client as CC

cmms = NC.NuvoloClient()
xdome = CC.ClarotyClient()

devices_cmms = cmms.search_devices(limit=1000, u_scripps_bio_active="true")
for device in devices_cmms.json().get("result", []):
    # print(f"{device.get('name')}")
    devices_xdome = xdome.get_devices(fields="asset_id", filter_by={
        "cmms_asset_tag": device.get('name'),
    }).json().get("result", [])
    if devices_xdome:
        print(f"  Found in XDome: {devices_xdome[0].get('asset_id')}")

