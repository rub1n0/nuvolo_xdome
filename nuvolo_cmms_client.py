import requests
from typing import Any, Dict, List, Optional


class NuvoloCMMSClient:
    """Simple client for Nuvolo CMMS built on ServiceNow's Table API."""

    def __init__(self, instance_url: str, username: str, password: str, table: str) -> None:
        """Create a client.

        Parameters
        ----------
        instance_url:
            Base URL to the ServiceNow instance, e.g. ``https://example.service-now.com``.
        username:
            Username used for basic authentication.
        password:
            Password for the user.
        table:
            Name of the table to interact with, e.g. ``cmdb_ci_computer``.
        """
        self.base_url = instance_url.rstrip('/')
        self.auth = (username, password)
        self.session = requests.Session()
        self.table = table
        self.path = f"{self.base_url}/api/now/table/{table}"
        # Accept JSON responses and send JSON payloads by default
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def get_record(self, sys_id: str, sysparm_fields: str | None = None) -> Dict[str, Any]:
        """Retrieve a single record by ``sys_id``."""
        params = {"sysparm_fields": sysparm_fields} if sysparm_fields else None
        resp = self.session.get(f"{self.path}/{sys_id}", params=params, auth=self.auth)
        resp.raise_for_status()
        return resp.json().get("result", {})
