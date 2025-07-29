import os
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv


class ClarotyClient:
    """Simple client for the Claroty xDome API."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None) -> None:
        load_dotenv()
        self.base_url = (base_url or os.getenv("CLAROTY_BASE_URL") or "https://api.medigate.io").rstrip("/")
        self.api_key = api_key or os.getenv("CLAROTY_API_KEY")
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"

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
    response = client.get_cmms_assets(fields=["cmms_uid"], limit=1)
    print(response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)


if __name__ == "__main__":
    main()
