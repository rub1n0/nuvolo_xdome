import json
import os
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv


class ClarotyClient:
    """Simple client for the Claroty xDome API."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None) -> None:
        load_dotenv()
        self.base_url = base_url or os.getenv("CLAROTY_BASE_URL")
        self.api_key = api_key or os.getenv("CLAROTY_API_KEY")

        if not self.base_url or not self.api_key:
            raise ValueError(
                "CLAROTY_BASE_URL and CLAROTY_API_KEY must be provided either "
                "via environment variables or as arguments."
            )

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def _request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.request(method, url, headers=self.headers, **kwargs)

    # CMMS assets endpoints
    def get_cmms_assets(self, *, fields: List[str], filter_by: Optional[Dict[str, Any]] = None,
                        include_count: bool = False, limit: int = 100, offset: int = 0,
                        sort_by: Optional[List[Dict[str, Any]]] = None) -> requests.Response:
        payload: Dict[str, Any] = {
            "fields": fields,
            "include_count": include_count,
            "limit": limit,
            "offset": offset,
        }
        if filter_by is not None:
            payload["filter_by"] = filter_by
        if sort_by is not None:
            payload["sort_by"] = sort_by
        return self._request("POST", "/api/v1/cmms/assets", json=payload)

    def add_cmms_assets(self, assets: List[Dict[str, Any]]) -> requests.Response:
        return self._request("POST", "/api/v1/cmms/assets/add", json={"assets": assets})

    def delete_cmms_assets(self, filter_by: Dict[str, Any]) -> requests.Response:
        return self._request("POST", "/api/v1/cmms/assets/delete", json={"filter_by": filter_by})

    def start_matching(self) -> requests.Response:
        return self._request("POST", "/api/v1/cmms/match")

    def get_match_status(self, task_id: str) -> requests.Response:
        return self._request("POST", "/api/v1/cmms/match/status", json={"task_id": task_id})

    # Device endpoints
    def get_devices(self, *, fields: List[str], filter_by: Optional[Dict[str, Any]] = None,
                    include_count: bool = False, limit: int = 100, offset: int = 0,
                    sort_by: Optional[List[Dict[str, Any]]] = None) -> requests.Response:
        payload: Dict[str, Any] = {
            "fields": fields,
            "include_count": include_count,
            "limit": limit,
            "offset": offset,
        }
        if filter_by is not None:
            payload["filter_by"] = filter_by
        if sort_by is not None:
            payload["sort_by"] = sort_by
        return self._request("POST", "/api/v1/devices/", json=payload)

    # Custom attribute endpoints
    def replace_custom_attribute(self, params: Dict[str, Any]) -> requests.Response:
        """Replace the values of a custom attribute."""
        return self._request("POST", "/api/v1/custom-attributes/replace", json=params)

    def set_custom_attribute(self, params: Dict[str, Any]) -> requests.Response:
        """Set values for a custom attribute."""
        return self._request("POST", "/api/v1/custom-attributes/set", json=params)


def main() -> None:
    client = ClarotyClient()
    # Example: check API connectivity by requesting empty match status (will likely fail without real task_id)
    response = client.get_devices(fields=[
        "active_queries_seen_reported_from",
        "ae_titles",
        "ap_location_list",
        "ap_name_list",
        "applied_acl_list",
        "applied_acl_type_list",
        "asset_id",
        "assignees",
        "authentication_user_list",
        "avg_examinations_per_day",
        "avg_in_use_per_day",
        "avg_online_per_day",
        "battery_level",
        "bssid_list",
        "cmdb_asset_tag",
        "cmms_asset_purchase_cost",
        "cmms_asset_tag",
        "cmms_building",
        "cmms_campus",
        "cmms_department",
        "cmms_financial_cost",
        "cmms_floor",
        "cmms_last_pm",
        "cmms_location",
        "cmms_manufacturer",
        "cmms_model",
        "cmms_ownership",
        "cmms_room",
        "cmms_serial_number",
        "cmms_state",
        "cmms_technician",
        "cmms_owning_cost_center",
        "collection_interfaces",
        "collection_interfaces_seen_reported_from",
        "collection_servers",
        "collection_servers_seen_reported_from",
        "combined_os",
        "connection_paths",
        "connection_type_list",
        "consequence_of_failure",
        "cppm_authentication_status_list",
        "cppm_roles_list",
        "cppm_service_list",
        "data_sources_seen_reported_from",
        "detector_name",
        "device_category",
        "device_name",
        "device_subcategory",
        "device_type",
        "device_type_family",
        "dhcp_fingerprint",
        "dhcp_hostnames",
        "dhcp_last_seen_hostname",
        "domains",
        "edge_hosts_seen_reported_from",
        "edge_locations",
        "edge_locations_seen_reported_from",
        "effective_likelihood_subscore",
        "effective_likelihood_subscore_points",
        "edr_is_up_to_date_text",
        "edr_last_scan_time",
        "enforcement_or_authorization_profiles_list",
        "equipment_class",
        "fda_class",
        "financial_cost",
        "first_seen_list",
        "handles_pii",
        "hardware_or_firmware_version",
        "hw_version",
        "http_hostnames",
        "http_last_seen_hostname",
        "infected",
        "integration_types_reported_from",
        "integrations_reported_from",
        "internet_communication",
        "ip_assignment_list",
        "ip_list",
        "is_online",
        "known_vulnerabilities",
        "known_vulnerabilities_points",
        "labels",
        "last_domain_user",
        "last_domain_user_activity",
        "last_edge_location_seen_reported_from",
        "last_project_file_path_reported_from",
        "last_scan_time",
        "last_seen_list",
        "last_seen_on_switch_list",
        "last_seen_reported",
        "likelihood_subscore",
        "likelihood_subscore_points",
        "local_name",
        "mac_list",
        "mac_oui_list",
        "machine_type",
        "managed_by",
        "management_services",
        "manufacturer",
        "mdm_compliance_status",
        "mdm_enrollment_status",
        "mdm_ownership",
        "model",
        "model_family",
        "mobility",
        "network_list",
        "network_scope_list",
        "note",
        "number_of_nics",
        "operating_hours_pattern_name",
        "organization_firewall_group_name",
        "organization_zone_name",
        "os_category",
        "os_eol_date",
        "os_name",
        "os_revision",
        "os_subcategory",
        "os_version",
        "other_hostnames",
        "phi",
        "purdue_level",
        "purdue_level_source",
        "product_code",
        "protocol_location_list",
        "recommended_firewall_group_name",
        "recommended_zone_name",
        "retired",
        "retired_since",
        "risk_score",
        "risk_score_points",
        "serial_number",
        "site_group_name",
        "site_name",
        "slot_cards",
        "snmp_hostnames",
        "snmp_last_seen_hostname",
        "software_or_firmware_version",
        "sort_by",
        "ssid_list",
        "suspicious",
        "switch_device_type_list",
        "switch_group_name_list",
        "switch_ip_list",
        "switch_location_list",
        "switch_mac_list",
        "switch_name_list",
        "switch_port_description_list",
        "switch_port_list",
        "uid",
        "utilization_rate",
        "vlan_description_list",
        "vlan_list",
        "vlan_name_list",
        "visibility_score",
        "visibility_score_level",
        "wlc_location_list",
        "wlc_name_list",
        "wifi_last_seen_list",
        "windows_hostnames",
        "windows_last_seen_hostname",
        "wireless_encryption_type_list"
    ], limit=1)
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.status_code)
        print(response.text)


if __name__ == "__main__":
    main()
