from multiprocessing import process
from unicodedata import name
import requests

INSTANCE_NUVOLO = process.env.get('INSTANCE_NUVOLO')
USER_NUVOLO = process.env.get('USER_NUVOLO')
PASSWORD_NUVOLO = process.env.get('PASSWORD_NUVOLO')
TABLE_NUVOLO = process.env.get('TABLE_NUVOLO')
ip_address = "192.168.1.1"
ip_list = ["192.168.1.1","192.168.1.2"]
sys_id = "fd7c101cebcb6e10b8ceff47bad0cd99"

def get_devices(sys_id, name, limit=20):
    url = f'https://{process.env.get("INSTANCE_NUVOLO")}.service-now.com/api/now/table/{process.env.get("TABLE_NUVOLO")}'
    params = {
        'sysparm_fields': f"{sys_id},{name}",
        'sysparm_limit': limit
    }
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, auth=(process.env.get("USER_NUVOLO"), process.env.get("PASSWORD_NUVOLO")), headers=headers, params=params)
    return response

def update_ip_address(sys_id, ip_address):
    url = f'https://{process.env.get("INSTANCE_NUVOLO")}.service-now.com/api/now/table/{process.env.get("TABLE_NUVOLO")}/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_address': ip_address
    }
    response = requests.patch(url, auth=(process.env.get("USER_NUVOLO"), process.env.get("PASSWORD_NUVOLO")), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to {ip_address} for sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def add_multiple_ips(sys_id, ip_list):
    ip_addresses = '\n'.join(ip_list)
    url = f'https://{process.env.get("INSTANCE_NUVOLO")}.service-now.com/api/now/table/{process.env.get("TABLE_NUVOLO")}/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_addresses': ip_addresses
    }
    response = requests.patch(url, auth=(process.env.get("USER_NUVOLO"), process.env.get("PASSWORD_NUVOLO")), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to:\n{ip_addresses}\nfor sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def main():
    response = add_multiple_ips(sys_id, ip_list)
    # update_ip_address(sys_id, ip_address)

    print(response)

if __name__ == '__main__':
    main()