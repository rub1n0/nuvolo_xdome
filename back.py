import requests

INSTANCE = 'scrippscmms'
USER = 'svc_xdome_rest'
PASSWORD = 'Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC'
TABLE = 'x_nuvo_eam_clinical_devices'
ip_address = '192.168.1.1'
ip_list = ['192.168.1.1', '192.168.1.2', '192.368.1.3']
sys_id = 'fd7c101cebcb6e10b8ceff47bad0cd99'

def get_devices(instance, user, password, table, limit=20):
    url = f'https://{instance}.service-now.com/api/now/table/{table}'
    params = {
        'sysparm_fields': 'sys_id,name',
        'sysparm_limit': limit
    }
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, auth=(user, password), headers=headers, params=params)
    return response

def print_devices(response):
    if response.status_code == 200:
        results = response.json().get('result', [])
        for record in results:
            print(f"sys_id: {record.get('sys_id')}, name: {record.get('name')}")
    else:
        print(f'Error: {response.status_code} - {response.text}')

def update_ip_address(instance, user, password, table, sys_id, ip_address):
    url = f'https://{instance}.service-now.com/api/now/table/{table}/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_address': ip_address
    }
    response = requests.patch(url, auth=(user, password), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to {ip_address} for sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def add_multiple_ips(instance, user, password, table, sys_id, ip_list):
    """
    Adds multiple IPs to the ip_addresses field, each on a new line.
    """
    ip_addresses = '\n'.join(ip_list)
    url = f'https://{instance}.service-now.com/api/now/table/{table}/{sys_id}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'ip_addresses': ip_addresses
    }
    response = requests.patch(url, auth=(user, password), headers=headers, json=data)
    if response.status_code in (200, 204):
        print(f"Successfully updated ip_addresses to:\n{ip_addresses}\nfor sys_id {sys_id}")
    else:
        print(f"Failed to update: {response.status_code} - {response.text}")

def main():
    # response = get_devices(INSTANCE, USER, PASSWORD, TABLE)
    response = add_multiple_ips(INSTANCE, USER, PASSWORD, TABLE, sys_id, ip_list)
    # update_ip_address(INSTANCE, USER, PASSWORD, TABLE, sys_id, ip_address)

    print(response)

if __name__ == '__main__':
    main()