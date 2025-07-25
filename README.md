# nuvolo_xdome

This repository provides a lightweight integration layer between **Nuvolo CMMS** and **Claroty xDome**.

## Overview

The package exposes client classes for each platform and an `IntegrationEngine` that can move records from one system to the other. The Nuvolo functions mirror the examples in `example.py` which demonstrate how to call ServiceNow's Table API.

For the Claroty API, the implementation follows the steps described in the ["To Construct an API Request"](https://help.medigate.io/hc/en-us/articles/10466430351005-xDome-API) documentation.

## Basic Usage

```python
from nuvolo_xdome import NuvoloCMMSClient, ClarotyXDomeClient, IntegrationEngine

nuvolo = NuvoloCMMSClient("https://instance.service-now.com", "user", "pass")
xdome = ClarotyXDomeClient("https://xdome.example.com/api/v1", "API_KEY")

engine = IntegrationEngine(nuvolo, xdome)

# search assets
assets = nuvolo.search_records("x_nuvo_eam_clinical_devices", sysparm_limit=5)

# update a record in Nuvolo
nuvolo.update_record("x_nuvo_eam_clinical_devices", "<sys_id>", {"ip_address": "10.0.0.1"})

# add a new record to xDome
xdome.add_record("assets", {"name": "Example"})
```
