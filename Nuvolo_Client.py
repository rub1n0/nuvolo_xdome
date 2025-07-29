from __future__ import annotations

import json

from nuvolo_cmms_client import NuvoloCMMSClient


def main() -> None:
    client = NuvoloCMMSClient()
    response = client.get_devices(limit=1)
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.status_code)
        print(response.text)


if __name__ == "__main__":
    main()
