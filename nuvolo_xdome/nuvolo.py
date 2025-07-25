import requests
from typing import Any, Dict, List, Optional

class NuvoloCMMSClient:
    """Client for Nuvolo CMMS built on ServiceNow."""

    def __init__(self, base_url: str, username: str, password: str, table: str = "alm_asset") -> None:
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({"Content-Type": "application/json"})
        self.table = table

    def add_asset(self, asset: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new asset to Nuvolo."""
        url = f"{self.base_url}/api/now/table/{self.table}"
        response = self.session.post(url, json=asset)
        response.raise_for_status()
        return response.json().get("result", {})

    def update_asset(self, sys_id: str, asset: Dict[str, Any]) -> Dict[str, Any]:
        """Update an asset in Nuvolo."""
        url = f"{self.base_url}/api/now/table/{self.table}/{sys_id}"
        response = self.session.put(url, json=asset)
        response.raise_for_status()
        return response.json().get("result", {})

    def search_assets(self, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Search Nuvolo assets using query parameters."""
        url = f"{self.base_url}/api/now/table/{self.table}"
        response = self.session.get(url, params=query or {})
        response.raise_for_status()
        return response.json().get("result", [])
