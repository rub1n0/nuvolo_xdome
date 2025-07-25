from typing import Any, Dict, List

from .claroty import ClarotyXDomeClient
from .nuvolo import NuvoloCMMSClient

class IntegrationEngine:
    """Engine that synchronizes assets between Nuvolo and Claroty xDome."""

    def __init__(self, nuvolo: NuvoloCMMSClient, xdome: ClarotyXDomeClient) -> None:
        self.nuvolo = nuvolo
        self.xdome = xdome

    def push_nuvolo_asset_to_xdome(self, sys_id: str) -> Dict[str, Any]:
        assets = self.nuvolo.search_assets({"sys_id": sys_id})
        if not assets:
            raise ValueError(f"Asset {sys_id} not found in Nuvolo")
        asset = assets[0]
        return self.xdome.add_asset(asset)

    def push_xdome_asset_to_nuvolo(self, asset_id: str) -> Dict[str, Any]:
        assets = self.xdome.search_assets({"id": asset_id})
        if not assets:
            raise ValueError(f"Asset {asset_id} not found in xDome")
        asset = assets[0]
        return self.nuvolo.add_asset(asset)

    def sync_updates_from_xdome(self, asset_id: str) -> Dict[str, Any]:
        assets = self.xdome.search_assets({"id": asset_id})
        if not assets:
            raise ValueError(f"Asset {asset_id} not found in xDome")
        asset = assets[0]
        sys_id = asset.get("sys_id")
        if not sys_id:
            raise ValueError("xDome asset missing sys_id for Nuvolo")
        return self.nuvolo.update_asset(sys_id, asset)

    def sync_updates_from_nuvolo(self, sys_id: str) -> Dict[str, Any]:
        assets = self.nuvolo.search_assets({"sys_id": sys_id})
        if not assets:
            raise ValueError(f"Asset {sys_id} not found in Nuvolo")
        asset = assets[0]
        asset_id = asset.get("id")
        if not asset_id:
            raise ValueError("Nuvolo asset missing id for xDome")
        return self.xdome.update_asset(asset_id, asset)

__all__ = [
    "ClarotyXDomeClient",
    "NuvoloCMMSClient",
    "IntegrationEngine",
]
