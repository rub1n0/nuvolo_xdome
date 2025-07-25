import requests
from typing import Any, Dict, Optional


class NuvoloCMMSClient:
    """Simple wrapper for ServiceNow Table API used by Nuvolo."""

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

    def search_records(self, table: str, **params: Any) -> Any:
        resp = self.session.get(self._url(table), params=params)
        resp.raise_for_status()
        return resp.json().get("result", [])

    def get_record(self, table: str, record_id: str) -> Any:
        resp = self.session.get(self._url(table, record_id))
        resp.raise_for_status()
        return resp.json().get("result")

    def add_record(self, table: str, data: Dict[str, Any]) -> Any:
        resp = self.session.post(self._url(table), json=data)
        resp.raise_for_status()
        return resp.json().get("result")

    def update_record(self, table: str, record_id: str, data: Dict[str, Any]) -> Any:
        resp = self.session.patch(self._url(table, record_id), json=data)
        resp.raise_for_status()
        return resp.json().get("result")


class ClarotyXDomeClient:
    """Client helper for Claroty xDome API."""

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

    def search_records(self, path: str, **params: Any) -> Any:
        return self._request("get", path, params=params)

    def add_record(self, path: str, data: Dict[str, Any]) -> Any:
        return self._request("post", path, json=data)

    def update_record(self, path: str, data: Dict[str, Any]) -> Any:
        return self._request("patch", path, json=data)


class IntegrationEngine:
    """Synchronizes records between Nuvolo and xDome."""

    def __init__(self, nuvolo: NuvoloCMMSClient, xdome: ClarotyXDomeClient) -> None:
        self.nuvolo = nuvolo
        self.xdome = xdome

    def push_nuvolo_record_to_xdome(self, table: str, sys_id: str, xdome_path: str) -> Any:
        record = self.nuvolo.get_record(table, sys_id)
        if record is None:
            raise ValueError("Record not found in Nuvolo")
        return self.xdome.add_record(xdome_path, record)

    def push_xdome_record_to_nuvolo(self, xdome_path: str, asset_id: str, table: str) -> Any:
        record = self.xdome.search_records(f"{xdome_path}/{asset_id}")
        if not record:
            raise ValueError("Record not found in xDome")
        return self.nuvolo.add_record(table, record)
