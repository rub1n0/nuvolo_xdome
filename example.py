import json
from unicodedata import name
import requests


ip_address = "192.168.1.1"
ip_list = ["192.168.1.1","192.168.1.2"]
sys_id = "fd7c101cebcb6e10b8ceff47bad0cd99"

def get_devices(limit=1):
    url = f'https://scrippscmms.service-now.com/api/now/table/x_nuvo_eam_clinical_devices'
    params = {
        'sysparm_limit': limit
    }
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, auth=("svc_xdome_rest", "Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC"), headers=headers, params=params)
    return response

def update_ip_address(sys_id, ip_address):
    url = f'https://scrippscmms.service-now.com/api/now/table/x_nuvo_eam_clinical_devices/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_address': ip_address
    }
    response = requests.patch(url, auth=("svc_xdome_rest", "Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC"), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to {ip_address} for sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def add_multiple_ips(sys_id, ip_list):
    ip_addresses = '\n'.join(ip_list)
    url = f'https://scrippscmms.service-now.com/api/now/table/x_nuvo_eam_clinical_devices/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_addresses': ip_addresses
    }
    response = requests.patch(url, auth=("svc_xdome_rest", "Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC"), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to:\n{ip_addresses}\nfor sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def main():
    print(json.dumps(get_devices().json(), indent=4))
    # update_ip_address(sys_id, ip_address)

if __name__ == '__main__':
    main()