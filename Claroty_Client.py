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
        "network_list",
        "device_category",
        "device_subcategory",
        "device_type",
        "uid",
        "detector_name",
        "asset_id",
        "mac_list",
        "ip_list",
        "device_type_family",
        "model",
        "model_family",
        "product_code",
        "os_category",
        "serial_number",
        "vlan_list",
        "retired",
        "labels",
        "assignees",
        "hw_version",
        "local_name",
        "os_name",
        "os_version",
        "os_revision",
        "os_subcategory",
        "combined_os",
        "endpoint_security_names",
        "equipment_class",
        "consequence_of_failure",
        "management_services",
        "ad_distinguished_name",
        "ad_description",
        "mdm_ownership",
        "mdm_enrollment_status",
        "mdm_compliance_status",
        "last_domain_user",
        "fda_class",
        "mobility",
        "purdue_level",
        "purdue_level_source",
        "dhcp_hostnames",
        "http_hostnames",
        "snmp_hostnames",
        "windows_hostnames",
        "other_hostnames",
        "windows_last_seen_hostname",
        "dhcp_last_seen_hostname",
        "http_last_seen_hostname",
        "snmp_last_seen_hostname",
        "ae_titles",
        "dhcp_fingerprint",
        "note",
        "domains",
        "battery_level",
        "internet_communication",
        "financial_cost",
        "handles_pii",
        "machine_type",
        "phi",
        "cmms_state",
        "cmms_ownership",
        "cmms_asset_tag",
        "cmms_campus",
        "cmms_building",
        "cmms_location",
        "cmms_floor",
        "cmms_department",
        "cmms_owning_cost_center",
        "cmms_asset_purchase_cost",
        "cmms_room",
        "cmms_manufacturer",
        "cmms_model",
        "cmms_serial_number",
        "cmms_last_pm",
        "cmms_technician",
        "edr_is_up_to_date_text",
        "avg_in_use_per_day",
        "avg_online_per_day",
        "avg_examinations_per_day",
        "mac_oui_list",
        "ip_assignment_list",
        "protocol_location_list",
        "vlan_name_list",
        "vlan_description_list",
        "connection_type_list",
        "ssid_list",
        "bssid_list",
        "wireless_encryption_type_list",
        "ap_name_list",
        "ap_location_list",
        "switch_mac_list",
        "switch_ip_list",
        "switch_name_list",
        "switch_port_list",
        "switch_location_list",
        "switch_port_description_list",
        "wlc_name_list",
        "wlc_location_list",
        "applied_acl_list",
        "applied_acl_type_list",
        "operating_hours_pattern_name",
        "collection_servers",
        "edge_locations",
        "last_edge_location_seen_reported_from",
        "integration_types_reported_from",
        "integrations_reported_from",
        "last_project_file_path_reported_from",
        "number_of_nics",
        "last_domain_user_activity",
        "last_scan_time",
        "edr_last_scan_time",
        "retired_since",
        "utilization_rate",
        "activity_rate",
        "os_eol_date",
        "last_seen_list",
        "first_seen_list",
        "wifi_last_seen_list",
        "last_seen_on_switch_list",
        "is_online",
        "network_scope_list",
        "end_of_life_state",
        "end_of_sale_date",
        "end_of_life_date",
        "connection_paths",
        "ise_authentication_method_list",
        "ise_endpoint_profile_list",
        "ise_identity_group_list",
        "ise_security_group_name_list",
        "ise_security_group_tag_list",
        "ise_logical_profile_list",
        "cppm_authentication_status_list",
        "cppm_roles_list",
        "cppm_service_list",
        "visibility_score",
        "visibility_score_level",
        "device_name",
        "manufacturer",
        "site_name",
        "site_group_name",
        "risk_score",
        "risk_score_points",
        "effective_likelihood_subscore",
        "effective_likelihood_subscore_points",
        "likelihood_subscore",
        "likelihood_subscore_points",
        "impact_subscore",
        "impact_subscore_points",
        "known_vulnerabilities",
        "known_vulnerabilities_points",
        "insecure_protocols",
        "insecure_protocols_points",
        "suspicious",
        "switch_group_name_list",
        "switch_device_type_list",
        "cmdb_asset_tag",
        "infected",
        "managed_by",
        "authentication_user_list",
        "collection_interfaces",
        "data_sources_seen_reported_from",
        "collection_servers_seen_reported_from",
        "collection_interfaces_seen_reported_from",
        "active_queries_seen_reported_from",
        "edge_hosts_seen_reported_from",
        "edge_locations_seen_reported_from",
        "last_seen_reported",
        "slot_cards",
        "cmms_financial_cost",
        "software_or_firmware_version",
        "enforcement_or_authorization_profiles_list",
        "ise_security_group_description_list",
        "recommended_firewall_group_name",
        "organization_firewall_group_name",
        "recommended_zone_name",
        "organization_zone_name"
    ], limit=1)
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.status_code)
        print(response.text)


if __name__ == "__main__":
    main()
