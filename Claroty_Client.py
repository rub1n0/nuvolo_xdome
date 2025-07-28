import os
from dotenv import load_dotenv
import requests

load_dotenv()
# Load environment variables
instance_url = os.getenv("INSTANCE_CLAROTY")
assets_endpoint = os.getenv("TABLE_CLAROTY")
api_key = os.getenv("API_KEY_CLAROTY")

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}' if api_key else None,
}

def asset_url(asset_id: str) -> str:
    # Return the API URL for a specific asset record.
    return f"{instance_url}{assets_endpoint}/{asset_id}"


def patch_asset(asset_id: str, data: dict) -> requests.Response:
    # Helper used by setters to send PATCH requests.
    return requests.patch(
        asset_url(asset_id),
        headers=headers,
        json=data,
    )


def get_assets(limit: int = 1) -> requests.Response:
    params = {"limit": limit}
    response = requests.get(
        instance_url + assets_endpoint,
        headers=headers,
        params=params,
    )
    return response


def search_assets(
    asset_id: str | None = None,
    asset_tag: str | None = None,
    limit: int = 10,
) -> requests.Response:
    params = {"limit": limit}
    query_parts = []
    if asset_id:
        query_parts.append(f"id={asset_id}")
    if asset_tag:
        query_parts.append(f"cmms_asset_tag={asset_tag}")
    if query_parts:
        params["query"] = "&".join(query_parts)
    response = requests.get(
        instance_url + assets_endpoint,
        headers=headers,
        params=params,
    )
    return response


def set_cmms_asset_tag(asset_id: str, asset_tag: str) -> None:
    data = {'cmms_asset_tag': asset_tag}
    response = patch_asset(asset_id, data)
    if response.status_code in (200, 204):
        log_action(f"{asset_id} - Successfully updated CMMS Asset Tag to: {asset_tag}")
    else:
        log_action(
            f"{asset_id} - Failed to update CMMS Asset Tag: {response.status_code} - {response.text}"
        )


def set_cmms_state(asset_id: str, state: str) -> None:
    data = {'cmms_state': state}
    response = patch_asset(asset_id, data)
    if response.status_code in (200, 204):
        log_action(f"{asset_id} - Successfully updated CMMS State to: {state}")
    else:
        log_action(
            f"{asset_id} - Failed to update CMMS State: {response.status_code} - {response.text}"
        )


def set_cmms_site(asset_id: str, site: str) -> None:
    data = {'cmms_site': site}
    response = patch_asset(asset_id, data)
    if response.status_code in (200, 204):
        log_action(f"{asset_id} - Successfully updated CMMS Site to: {site}")
    else:
        log_action(
            f"{asset_id} - Failed to update CMMS Site: {response.status_code} - {response.text}"
        )


def set_cmms_building(asset_id: str, building: str) -> None:
    data = {'cmms_building': building}
    response = patch_asset(asset_id, data)
    if response.status_code in (200, 204):
        log_action(f"{asset_id} - Successfully updated CMMS Building to: {building}")
    else:
        log_action(
            f"{asset_id} - Failed to update CMMS Building: {response.status_code} - {response.text}"
        )


def set_cmms_cost_center(asset_id: str, cost_center: str) -> None:
    data = {'cmms_cost_center': cost_center}
    response = patch_asset(asset_id, data)
    if response.status_code in (200, 204):
        log_action(f"{asset_id} - Successfully updated CMMS Cost Center to: {cost_center}")
    else:
        log_action(
            f"{asset_id} - Failed to update CMMS Cost Center: {response.status_code} - {response.text}"
        )


def log_action(action: str) -> None:
    print(f"[+] {action}")


if __name__ == "__main__":
    pass
