# nuvolo_xdome

This package provides a simple integration engine between **Nuvolo CMMS** (built on ServiceNow) and **Claroty xDome**.  It exposes Python clients for both platforms and an `IntegrationEngine` class that can synchronize assets between them.

The xDome API is documented at <https://help.medigate.io/hc/en-us/articles/10466430351005-xDome-API>.  The Nuvolo API relies on ServiceNow's Table API endpoints.

## Installation

The library requires the `requests` package:

```bash
pip install requests
```

## Usage Example

```python
from nuvolo_xdome import ClarotyXDomeClient, NuvoloCMMSClient, IntegrationEngine

nuvolo = NuvoloCMMSClient("https://nuvolo.example.com", "user", "pass")
xdome = ClarotyXDomeClient("https://xdome.example.com/api/v1", "API_KEY")

engine = IntegrationEngine(nuvolo, xdome)
engine.push_nuvolo_asset_to_xdome("<nuvolo_sys_id>")
```

## Library Overview

- **NuvoloCMMSClient** – wrappers for the ServiceNow Table API to search, create and update asset records.
- **ClarotyXDomeClient** – simplified helper for xDome API requests following the "To Construct an API Request" section of the Claroty documentation.
- **IntegrationEngine** – utility methods to push assets from one platform to the other.

Each client maintains an internal `requests.Session` with the proper authentication headers so repeated calls are straightforward.

