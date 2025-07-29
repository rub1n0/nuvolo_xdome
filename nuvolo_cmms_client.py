import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv


class NuvoloCMMSClient:
    """Client for interacting with the Nuvolo CMMS API."""

    def __init__(
        self,
        *,
        instance_url: Optional[str] = None,
        devices_table: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        load_dotenv()
        self.instance_url = instance_url or os.getenv("NUVOLO_INSTANCE")
        self.devices_table = devices_table or os.getenv("NUVOLO_DEVICES_TABLE")
        user = username or os.getenv("NUVOLO_USER")
        pw = password or os.getenv("NUVOLO_PASSWORD")

        if not all([self.instance_url, self.devices_table, user, pw]):
            raise ValueError(
                "NUVOLO_INSTANCE, NUVOLO_DEVICES_TABLE, NUVOLO_USER and "
                "NUVOLO_PASSWORD must be provided either via environment "
                "variables or as arguments."
            )

        self.auth = (user, pw)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = f"{self.instance_url}{path}"
        return requests.request(method, url, auth=self.auth, headers=self.headers, **kwargs)

    # basic device operations
    def get_devices(self, limit: int = 1) -> requests.Response:
        params = {"sysparm_limit": limit}
        return self._request("GET", self.devices_table, params=params)

    def search_devices(self, limit: int = 10, **criteria: Optional[str]) -> requests.Response:
        params = {"sysparm_limit": limit}
        query = "^".join(f"{k}={v}" for k, v in criteria.items() if v is not None)
        if query:
            params["sysparm_query"] = query
        return self._request("GET", self.devices_table, params=params)

    def update_device(self, sys_id: str, data: Dict[str, Any]) -> requests.Response:
        path = f"{self.devices_table}/{sys_id}"
        return self._request("PATCH", path, json=data)

    def update_field(self, sys_id: str, field: str, value: Any) -> requests.Response:
        return self.update_device(sys_id, {field: value})


if __name__ == "__main__":
    client = NuvoloCMMSClient()
    response = client.get_devices(limit=1)
    try:
        print(response.json())
    except Exception:
        print(response.status_code)
        print(response.text)
