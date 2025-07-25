import requests
from typing import Any, Dict, List, Optional

class ClarotyXDomeClient:
    """Client for Claroty xDome asset API.

    Parameters are described in the official documentation:
    https://help.medigate.io/hc/en-us/articles/10466430351005-xDome-API
    """

    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        })

    def add_asset(self, asset: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new asset to xDome."""
        url = f"{self.base_url}/assets"
        response = self.session.post(url, json=asset)
        response.raise_for_status()
        return response.json()

    def update_asset(self, asset_id: str, asset: Dict[str, Any]) -> Dict[str, Any]:
        """Update an asset in xDome."""
        url = f"{self.base_url}/assets/{asset_id}"
        response = self.session.put(url, json=asset)
        response.raise_for_status()
        return response.json()

    def search_assets(self, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Search xDome assets using query parameters."""
        url = f"{self.base_url}/assets"
        response = self.session.get(url, params=query or {})
        response.raise_for_status()
        return response.json().get("assets", [])
