import requests
from typing import Any, Dict, Optional


class NuvoloCMMSClient:
    """Simple client for interacting with Nuvolo CMMS via ServiceNow's Table API."""

    def __init__(self, instance_url: str, username: str, password: str) -> None:
        self.instance_url = instance_url.rstrip('/')
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _url(self, table: str, record_id: Optional[str] = None) -> str:
        base = f"{self.instance_url}/api/now/table/{table}"
        if record_id:
            base += f"/{record_id}"
        return base

    def search_assets(self, table: str, **params: Any) -> Any:
        resp = self.session.get(self._url(table), params=params)
        resp.raise_for_status()
        return resp.json().get("result", [])

    def get_asset(self, table: str, record_id: str) -> Any:
        resp = self.session.get(self._url(table, record_id))
        resp.raise_for_status()
        return resp.json().get("result")

    def create_asset(self, table: str, data: Dict[str, Any]) -> Any:
        resp = self.session.post(self._url(table), json=data)
        resp.raise_for_status()
        return resp.json().get("result")

    def update_asset(self, table: str, record_id: str, data: Dict[str, Any]) -> Any:
        resp = self.session.patch(self._url(table, record_id), json=data)
        resp.raise_for_status()
        return resp.json().get("result")


class ClarotyXDomeClient:
    """Client for Claroty xDome API."""

    def __init__(self, base_url: str, api_key: str, verify: bool = True) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.verify = verify
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        resp = self.session.request(method, self._url(path), **kwargs)
        resp.raise_for_status()
        try:
            return resp.json()
        except ValueError:
            return resp.text

    def search_assets(self, **params: Any) -> Any:
        return self._request("get", "assets", params=params)

    def get_asset(self, asset_id: str) -> Any:
        return self._request("get", f"assets/{asset_id}")

    def create_asset(self, data: Dict[str, Any]) -> Any:
        return self._request("post", "assets", json=data)

    def update_asset(self, asset_id: str, data: Dict[str, Any]) -> Any:
        return self._request("patch", f"assets/{asset_id}", json=data)


class IntegrationEngine:
    """Synchronizes assets between Nuvolo and xDome."""

    def __init__(self, nuvolo: NuvoloCMMSClient, xdome: ClarotyXDomeClient) -> None:
        self.nuvolo = nuvolo
        self.xdome = xdome

    def push_nuvolo_asset_to_xdome(self, sys_id: str, table: str = "x_nuvo_eam_clinical_devices") -> Any:
        asset = self.nuvolo.get_asset(table, sys_id)
        if asset is None:
            raise ValueError("Asset not found in Nuvolo")
        return self.xdome.create_asset(asset)

    def push_xdome_asset_to_nuvolo(self, asset_id: str, table: str = "x_nuvo_eam_clinical_devices") -> Any:
        asset = self.xdome.get_asset(asset_id)
        if not asset:
            raise ValueError("Asset not found in xDome")
        return self.nuvolo.create_asset(table, asset)
