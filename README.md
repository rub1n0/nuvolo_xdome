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

