import json
import requests

sys_id = "fd7c101cebcb6e10b8ceff47bad0cd99"
instance_url = f'https://scrippscmms.service-now.com/api/now/table/'
devices_table = "x_nuvo_eam_clinical_devices"
instance_user = "svc_xdome_rest"
instance_password = "Xb_Ia}Dg9YdZyl#iNgYkowzv}0{Iq]dml^[gbs#Q$pbFoJHSBp:OI9bog6yAtX;{uvpWJoL_yE7K%:a!O#%]u.^FC$-,707Kg&ZC"
headers = {'Accept': 'application/json','Content-Type': 'application/json'}
url = f'{instance_url}/{sys_id}'


def get_devices(limit=1):
    params = {
        'sysparm_limit': limit
    }
    response = requests.get(instance_url + devices_table, auth=(instance_user, instance_password), headers=headers, params=params)
    return response

def search_devices(name=None, mac_addresses=None, model=None, serial_number=None, sysId=None, limit=10):
    params = {'sysparm_limit': limit}
    query_parts = []
    if name:
        query_parts.append(f"name={name}")
    if mac_addresses:
        query_parts.append(f"mac_addresses={mac_addresses}")
    if model:
        query_parts.append(f"model={model}")
    if serial_number:
        query_parts.append(f"serial_number={serial_number}")
    if sysId:
        query_parts.append(f"sys_id={sysId}")
    if query_parts:
        params['sysparm_query'] = '^'.join(query_parts)
    response = requests.get(
        instance_url + devices_table,
        auth=(instance_user, instance_password),
        headers=headers,
        params=params,
    )
    return response

def set_ips(sys_id, ip_list):
    ip_addresses = '\n'.join(ip_list)
    data = {
        'ip_addresses': ip_addresses
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ip_addresses to: {' '.join(ip_list)}")
    else:
        log_action(f"{sys_id} - Failed to add ip_addresses: {response.status_code} - {response.text}")

def set_macs(sys_id, mac_list):
    mac_addresses = '\n'.join(mac_list)
    data = {
        'mac_addresses': mac_addresses
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated mac_addresses to: {' '.join(mac_list)}")
    else:
        log_action(f"{sys_id} - Failed to add update mac_addresses: {response.status_code} - {response.text}")

def set_connection_type(sys_id, connection_type):
    data = {
        'u_connection_type': connection_type
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated connection_type to: {connection_type}")
    else:
        log_action(f"{sys_id} - Failed to add connection_type: {response.status_code} - {response.text}")

def set_site_name(sys_id, site_name):
    data = {
        'u_site_name': site_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated site_name to: {site_name}")
    else:
        log_action(f"{sys_id} - Failed to add site_name: {response.status_code} - {response.text}")

def set_xdome_id(sys_id, xdome_id):
    data = {
        'u_medigate_id': xdome_id
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated xdome_id to: {xdome_id}")
    else:
        log_action(f"{sys_id} - Failed to add xdome_id: {response.status_code} - {response.text}")

def set_network(sys_id, network):
    data = {
        'u_network': network
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated network to: {network}")
    else:
        log_action(f"{sys_id} - Failed to add network: {response.status_code} - {response.text}")

def set_xdome_category(sys_id, category):
    data = {
        'u_medigate_category': category
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated xdome_category to: {category}")
    else:
        log_action(f"{sys_id} - Failed to add xdome_category: {response.status_code} - {response.text}")

def set_xdome_sub_category(sys_id, sub_category):
    data = {
        'u_medigate_sub_category': sub_category
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated xdome_sub_category to: {sub_category}")
    else:
        log_action(f"{sys_id} - Failed to add xdome_sub_category: {response.status_code} - {response.text}")

def set_machine_type(sys_id, machine_type):
    data = {
        'u_machine_type': machine_type
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated machine_type to: {machine_type}")
    else:
        log_action(f"{sys_id} - Failed to add machine_type: {response.status_code} - {response.text}")

def set_mobility(sys_id, mobility):
    data = {
        'u_mobility': mobility
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated mobility to: {mobility}")
    else:
        log_action(f"{sys_id} - Failed to add mobility: {response.status_code} - {response.text}")

def set_os(sys_id, os):
    data = {
        'operating_system': os
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated os to: {os}")
    else:
        log_action(f"{sys_id} - Failed to add os: {response.status_code} - {response.text}")

def set_os_name(sys_id, os_name):
    data = {
        'u_os_name': os_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated os_name to: {os_name}")
    else:
        log_action(f"{sys_id} - Failed to add os_name: {response.status_code} - {response.text}")

def set_os_version(sys_id, os_version):
    data = {
        'u_os_version': os_version
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated os_version to: {os_version}")
    else:
        log_action(f"{sys_id} - Failed to add os_version: {response.status_code} - {response.text}")

def set_app_version(sys_id, app_version):
    data = {
        'u_app_version': app_version
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated app_version to: {app_version}")
    else:
        log_action(f"{sys_id} - Failed to add app_version: {response.status_code} - {response.text}")

def set_hw_version(sys_id, hw_version):
    data = {
        'u_hw_version': hw_version
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hw_version to: {hw_version}")
    else:
        log_action(f"{sys_id} - Failed to add hw_version: {response.status_code} - {response.text}")

def set_ae_title(sys_id, ae_title):
    data = {
        'x_ctv_htm_aet': ae_title
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ae_title to: {ae_title}")
    else:
        log_action(f"{sys_id} - Failed to add ae_title: {response.status_code} - {response.text}")

def set_domain_name(sys_id, domain_name):
    data = {
        'dns_name': domain_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated domain_name to: {domain_name}")
    else:
        log_action(f"{sys_id} - Failed to add domain_name: {response.status_code} - {response.text}")

def set_hostname_dhcp(sys_id, hostname_dhcp):
    data = {
        'u_hostname_dhcp': hostname_dhcp
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hostname_dhcp to: {hostname_dhcp}")
    else:
        log_action(f"{sys_id} - Failed to add hostname_dhcp: {response.status_code} - {response.text}")

def set_hostname_http(sys_id, hostname_http):
    data = {
        'u_hostname_http': hostname_http
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hostname_http to: {hostname_http}")
    else:
        log_action(f"{sys_id} - Failed to add hostname_http: {response.status_code} - {response.text}")

def set_hostname_snmp(sys_id, hostname_snmp):
    data = {
        'u_hostname_snmp': hostname_snmp
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hostname_snmp to: {hostname_snmp}")
    else:
        log_action(f"{sys_id} - Failed to add hostname_snmp: {response.status_code} - {response.text}")

def set_hostname_win(sys_id, hostname_win):
    data = {
        'u_hostname_win': hostname_win
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hostname_win to: {hostname_win}")
    else:
        log_action(f"{sys_id} - Failed to add hostname_win: {response.status_code} - {response.text}")

def set_hostname_other(sys_id, hostname_other):
    data = {
        'u_hostname_other': hostname_other
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated hostname_other to: {hostname_other}")
    else:
        log_action(f"{sys_id} - Failed to add hostname_other: {response.status_code} - {response.text}")

def set_dhcp_fingerlog_action(sys_id, dhcp_fingerprint):
    data = {
        'u_dhcp_fingerprint': dhcp_fingerprint
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated dhcp_fingerprint to: {dhcp_fingerprint}")
    else:
        log_action(f"{sys_id} - Failed to add dhcp_fingerprint: {response.status_code} - {response.text}")

def set_device_name_protocol(sys_id, device_name_protocol):
    data = {
        'u_device_name_protocol': device_name_protocol
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated device_name_protocol to: {device_name_protocol}")
    else:
        log_action(f"{sys_id} - Failed to add device_name_protocol: {response.status_code} - {response.text}")

def set_vlan(sys_id, vlan):
    data = {
        'u_vlan': vlan
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated vlan to: {vlan}")
    else:
        log_action(f"{sys_id} - Failed to add vlan: {response.status_code} - {response.text}")

def set_vlan_name(sys_id, vlan_name):
    data = {
        'u_vlan_name': vlan_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated vlan_name to: {vlan_name}")
    else:
        log_action(f"{sys_id} - Failed to add vlan_name: {response.status_code} - {response.text}")

def set_vlan_description(sys_id, vlan_description):
    data = {
        'u_vlan_description': vlan_description
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated vlan_description to: {vlan_description}")
    else:
        log_action(f"{sys_id} - Failed to add vlan_description: {response.status_code} - {response.text}")

def set_ip_assignment(sys_id, ip_assignment):
    data = {
        'u_ip_assignment': ip_assignment
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ip_assignment to: {ip_assignment}")
    else:
        log_action(f"{sys_id} - Failed to add ip_assignment: {response.status_code} - {response.text}")

def set_managed_device(sys_id, managed_device):
    data = {
        'u_managed_device': managed_device
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated managed_device to: {managed_device}")
    else:
        log_action(f"{sys_id} - Failed to add managed_device: {response.status_code} - {response.text}")

def set_wireless_encryption(sys_id, wireless_encryption):
    data = {
        'u_wireless_encryption': wireless_encryption
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated wireless_encryption to: {wireless_encryption}")
    else:
        log_action(f"{sys_id} - Failed to add wireless_encryption: {response.status_code} - {response.text}")

def set_last_seen(sys_id, last_seen):
    data = {
        'last_discovered': last_seen
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated last_seen to: {last_seen}")
    else:
        log_action(f"{sys_id} - Failed to add last_seen: {response.status_code} - {response.text}")

def set_location_protocol(sys_id, location_protocol):
    data = {
        'u_location_protocol': location_protocol
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated location_protocol to: {location_protocol}")
    else:
        log_action(f"{sys_id} - Failed to add location_protocol: {response.status_code} - {response.text}")

def set_ap_bssid(sys_id, ap_bssid):
    data = {
        'u_ap_bssid': ap_bssid
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ap_bssid to: {ap_bssid}")
    else:
        log_action(f"{sys_id} - Failed to add ap_bssid: {response.status_code} - {response.text}")

def set_ssid(sys_id, ssid):
    data = {
        'u_ssid': ssid
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ssid to: {ssid}")
    else:
        log_action(f"{sys_id} - Failed to add ssid: {response.status_code} - {response.text}")

def set_ap_name(sys_id, ap_name):
    data = {
        'u_ap_name': ap_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ap_name to: {ap_name}")
    else:
        log_action(f"{sys_id} - Failed to add ap_name: {response.status_code} - {response.text}")

def set_ap_location(sys_id, ap_location):
    data = {
        'u_ap_location': ap_location
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ap_location to: {ap_location}")
    else:
        log_action(f"{sys_id} - Failed to add ap_location: {response.status_code} - {response.text}")

def set_last_seen_on_ap(sys_id, last_seen_on_ap):
    data = {
        'u_last_seen_on_ap': last_seen_on_ap
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated last_seen_on_ap to: {last_seen_on_ap}")
    else:
        log_action(f"{sys_id} - Failed to add last_seen_on_ap: {response.status_code} - {response.text}")

def set_wlc_name(sys_id, wlc_name):
    data = {
        'u_wlc_name': wlc_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated wlc_name to: {wlc_name}")
    else:
        log_action(f"{sys_id} - Failed to add wlc_name: {response.status_code} - {response.text}")

def set_wlc_location(sys_id, wlc_location):
    data = {
        'u_wlc_location': wlc_location
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated wlc_location to: {wlc_location}")
    else:
        log_action(f"{sys_id} - Failed to add wlc_location: {response.status_code} - {response.text}")

def set_switch_ip(sys_id, switch_ip):
    data = {
        'u_switch_ip': switch_ip
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_ip to: {switch_ip}")
    else:
        log_action(f"{sys_id} - Failed to add switch_ip: {response.status_code} - {response.text}")

def set_switch_mac(sys_id, switch_mac):
    data = {
        'u_switch_mac': switch_mac
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_mac to: {switch_mac}")
    else:
        log_action(f"{sys_id} - Failed to add switch_mac: {response.status_code} - {response.text}")

def set_switch_port_id(sys_id, switch_port_id):
    data = {
        'u_switch_port_id': switch_port_id
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_port_id to: {switch_port_id}")
    else:
        log_action(f"{sys_id} - Failed to add switch_port_id: {response.status_code} - {response.text}")

def set_switch_port_description(sys_id, switch_port_description):
    data = {
        'u_switch_port_description': switch_port_description
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_port_description to: {switch_port_description}")
    else:
        log_action(f"{sys_id} - Failed to add switch_port_description: {response.status_code} - {response.text}")

def set_switch_name(sys_id, switch_name):
    data = {
        'u_switch_name': switch_name
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_name to: {switch_name}")
    else:
        log_action(f"{sys_id} - Failed to add switch_name: {response.status_code} - {response.text}")

def set_switch_location(sys_id, switch_location):
    data = {
        'u_switch_location': switch_location
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated switch_location to: {switch_location}")
    else:
        log_action(f"{sys_id} - Failed to add switch_location: {response.status_code} - {response.text}")

def set_last_seen_on_switch(sys_id, last_seen_on_switch):
    data = {
        'u_last_seen_on_switch': last_seen_on_switch
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated last_seen_on_switch to: {last_seen_on_switch}")
    else:
        log_action(f"{sys_id} - Failed to add last_seen_on_switch: {response.status_code} - {response.text}")

def set_risk_score(sys_id, risk_score): 
    data = {
        'u_cyber_risk_score': risk_score
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated risk_score to: {risk_score}")
    else:
        log_action(f"{sys_id} - Failed to add risk_score: {response.status_code} - {response.text}")

def set_device_vulnerability_score(sys_id, vulnerability_score):
    data = {
        'u_device_vulnerability_score': vulnerability_score
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated vulnerability_score to: {vulnerability_score}")
    else:
        log_action(f"{sys_id} - Failed to add device_vulnerability_score: {response.status_code} - {response.text}")

def set_device_severity_score(sys_id, severity_score):
    data = {
        'u_device_severity_score': severity_score
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated severity_score to: {severity_score}")
    else:
        log_action(f"{sys_id} - Failed to add device_severity_score: {response.status_code} - {response.text}")

def set_fda_classification(sys_id, fda_classification):
    data = {
        'u_fda_class': fda_classification
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated fda_classification to: {fda_classification}")
    else:
        log_action(f"{sys_id} - Failed to add fda_classification: {response.status_code} - {response.text}")

def set_phi(sys_id, phi):
    data = {
        'u_phi': phi
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated phi to: {phi}")
    else:
        log_action(f"{sys_id} - Failed to add phi: {response.status_code} - {response.text}")

def set_endpoint_security(sys_id, endpoint_security):
    data = {
        'u_endpoint_security': endpoint_security
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated endpoint_security to: {endpoint_security}")
    else:
        log_action(f"{sys_id} - Failed to add endpoint_security: {response.status_code} - {response.text}")

def set_ave_daily_usage(sys_id, ave_daily_usage):
    data = {
        'u_average_daily_usage': ave_daily_usage
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated ave_daily_usage to: {ave_daily_usage}")
    else:
        log_action(f"{sys_id} - Failed to add ave_daily_usage: {response.status_code} - {response.text}")

def set_utilization(sys_id, utilization):
    data = {
        'u_utilization': utilization
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated utilization to: {utilization}")
    else:
        log_action(f"{sys_id} - Failed to add utilization: {response.status_code} - {response.text}")

def set_link_to_xdome(sys_id, link_to_xdome):
    data = {
        'u_link_to_xdome': link_to_xdome
    }
    response = requests.patch(url, auth=(instance_user, instance_password), headers=headers, json=data)
    if response.status_code in (200, 204):
        log_action(f"{sys_id} - Successfully updated link_to_xdome to: {link_to_xdome}")
    else:
        log_action(f"{sys_id} - Failed to add link_to_xdome: {response.status_code} - {response.text}")

def log_action(action):
    print(f"[+] {action}")

def main():

    device_list = get_devices(10)
    if device_list.status_code == 200:
        data = device_list.json()
        print("Device List:")   
        for device in data.get('result', []):
            print(f"\t-> {device.get('name')}")
    else:
        log_action(f"Failed to fetch devices: {device_list.status_code} - {device_list.text}")

    search_result = search_devices(sysId="fd7c101cebcb6e10b8ceff47bad0cd99", limit=5)
    if search_result.status_code == 200:
        data = search_result.json()
        print("Search Results:")
        for device in data.get('result', []):
            print(f"\t-> {device.get('name')}")
    else:
        log_action(f"Failed to search devices: {search_result.status_code} - {search_result.text}")

### Example usage of the functions defined above
#  set_ips(sys_id, [""])
#  set_macs(sys_id, [""])
#  set_connection_type(sys_id, "")
#  set_site_name(sys_id, "")
#  set_xdome_id(sys_id, "")
#  set_network(sys_id, "")
#  set_xdome_category(sys_id, "")
#  set_xdome_sub_category(sys_id, "")
#  set_machine_type(sys_id, "")
#  set_phi(sys_id, "")
#  set_endpoint_security(sys_id, "")
#  set_ave_daily_usage(sys_id, None)
#  set_mobility(sys_id, "")
#  set_os(sys_id, "")
#  set_os_name(sys_id, "")
#  set_os_version(sys_id, "")
#  set_app_version(sys_id, "")
#  set_hw_version(sys_id, "")
#  set_ae_title(sys_id, "")
#  set_domain_name(sys_id, "")
#  set_hostname_dhcp(sys_id, "")
#  set_hostname_http(sys_id, "")
#  set_hostname_snmp(sys_id, "")
#  set_hostname_win(sys_id, "")
#  set_hostname_other(sys_id, "")
#  set_dhcp_fingerlog_action(sys_id, "")
#  set_device_name_protocol(sys_id, "")
#  set_vlan(sys_id, "")
#  set_vlan_name(sys_id, "")
#  set_vlan_description(sys_id, "")
#  set_ip_assignment(sys_id, "")
#  set_ap_bssid(sys_id, "")
#  set_ssid(sys_id, "")
#  set_ap_name(sys_id, "")
#  set_ap_location(sys_id, "")
#  set_last_seen_on_ap(sys_id, "")
#  set_wlc_name(sys_id, "")
#  set_wlc_location(sys_id, "")
#  set_switch_ip(sys_id, "")
#  set_switch_name(sys_id, "")
#  set_switch_location(sys_id, "")
#  set_switch_mac(sys_id, "")
#  set_switch_port_id(sys_id, "")
#  set_switch_port_description(sys_id, "")
#  set_last_seen_on_switch(sys_id, "")
#  set_location_protocol(sys_id, "")
#  set_risk_score(sys_id, None)
#  set_device_vulnerability_score(sys_id, None)
#  set_device_severity_score(sys_id, None)
#  set_fda_classification(sys_id, "")
#  set_phi(sys_id, "")
#  set_endpoint_security(sys_id, "")
#  set_ave_daily_usage(sys_id, None)
#  set_utilization(sys_id, None)
#  set_link_to_xdome(sys_id, "")
    
if __name__ == '__main__':
    main()