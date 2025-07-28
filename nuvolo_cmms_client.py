import requests
from typing import Any, Dict, List, Optional


class NuvoloCMMSClient:
    """Simple client for Nuvolo CMMS built on ServiceNow's Table API."""

    def __init__(self, instance_url: str, username: str, password: str) -> None:
        """Create a client.

        Parameters
        ----------
        instance_url:
            Base URL to the ServiceNow instance, e.g. ``https://example.service-now.com``.
        username:
            Username used for basic authentication.
        password:
            Password for the user.
        """
        self.base_url = instance_url.rstrip('/')
        self.auth = (username, password)
        self.session = requests.Session()
        # Accept JSON responses and send JSON payloads by default
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def _table_url(self, table: str, sys_id: Optional[str] = None) -> str:
        path = f"/api/now/table/{table}"
        if sys_id:
            path += f"/{sys_id}"
        return self.base_url + path

    def search_records(
        self,
        table: str,
        sysparm_query: str | None = None,
        sysparm_limit: int = 20,
        sysparm_fields: str | None = None,
    ) -> List[Dict[str, Any]]:
        """Search a table for records.

        Parameters mirror those of ServiceNow's Table API. ``sysparm_query`` can
        contain an encoded query; ``sysparm_fields`` controls which fields are
        returned.
        """
        params: Dict[str, Any] = {"sysparm_limit": sysparm_limit}
        if sysparm_query:
            params["sysparm_query"] = sysparm_query
        if sysparm_fields:
            params["sysparm_fields"] = sysparm_fields

        resp = self.session.get(self._table_url(table), params=params, auth=self.auth)
        resp.raise_for_status()
        data = resp.json()
        return data.get("result", [])

    def get_record(self, table: str, sys_id: str, sysparm_fields: str | None = None) -> Dict[str, Any]:
        """Retrieve a single record by ``sys_id``."""
        params = {"sysparm_fields": sysparm_fields} if sysparm_fields else None
        resp = self.session.get(self._table_url(table, sys_id), params=params, auth=self.auth)
        resp.raise_for_status()
        return resp.json().get("result", {})

    def update_record(self, table: str, sys_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Patch a record in ``table`` identified by ``sys_id`` with ``data``."""
        resp = self.session.patch(self._table_url(table, sys_id), json=data, auth=self.auth)
        resp.raise_for_status()
        return resp.json().get("result", {})

    def update_ip_address(self, table: str, sys_id: str, ip_address: str) -> Dict[str, Any]:
        """Convenience wrapper to update the ``ip_address`` field of a record."""
        return self.update_record(table, sys_id, {"ip_address": ip_address})

    def add_multiple_ips(self, table: str, sys_id: str, ip_list: List[str]) -> Dict[str, Any]:
        """Convenience wrapper that joins multiple IPs with newlines and updates the ``ip_addresses`` field."""
        ips = "\n".join(ip_list)
        return self.update_record(table, sys_id, {"ip_addresses": ips})
