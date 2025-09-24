# nuvolo_xdome

Utilities for synchronising device data between Claroty xDome and Nuvolo CMMS.

The repository contains:

- `Claroty_Client.py` – A minimal wrapper around the Claroty xDome REST API.
- `Nuvolo_Client.py` – A small client for the Nuvolo CMMS (ServiceNow) API.
- `engine.py` – A matching routine that compares CMMS device names against xDome asset tags.

All credentials are read from environment variables so that no secrets are stored in the source tree.

## Prerequisites

- Python 3.10+
- Access to Claroty xDome and Nuvolo CMMS APIs
- API credentials with permission to query the relevant endpoints

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

1. Copy `.env.example` to `.env`.
2. Replace the placeholder values with credentials for your environments.

| Variable | Description |
| --- | --- |
| `CLAROTY_BASE_URL` | Base URL of the Claroty xDome instance, e.g. `https://your-claroty-instance.example.com`. |
| `CLAROTY_API_KEY` | Claroty API token used for bearer authentication. |
| `NUVOLO_INSTANCE` | Base URL of the Nuvolo tenant, such as `https://your-instance.service-now.com`. |
| `NUVOLO_DEVICES_TABLE` | Path to the CMMS devices table (for example, `/api/now/table/u_devices`). |
| `NUVOLO_USER` | Username with API access to the Nuvolo instance. |
| `NUVOLO_PASSWORD` | Password (or token) for the Nuvolo API user. |

The clients use [`python-dotenv`](https://pypi.org/project/python-dotenv/) to automatically read the `.env` file when they are instantiated. Alternatively, export the variables via your shell.

## Usage

### Claroty client

```bash
python Claroty_Client.py
```

The script performs a sample request against the devices endpoint and prints the JSON response (or the HTTP status) so that you can confirm connectivity.

### Nuvolo client

```bash
python Nuvolo_Client.py
```

This retrieves a small batch of device records from Nuvolo. Adjust the logic or call `NuvoloClient` from your own scripts to perform CRUD operations.

### Matching engine

Run the matcher to locate xDome assets whose `cmdb_asset_tag` matches the CMMS `name` field:

```bash
python engine.py --threads 8 --limit 100
```

The command fetches devices from Nuvolo in batches (respecting the specified limit) and performs lookups in xDome concurrently. A progress bar from `tqdm` displays progress, and the script prints the number of matches found.

You can optionally scope the CMMS search to specific records by providing one or more `--filter` arguments using ServiceNow query syntax:

```bash
python engine.py --filter install_status=1 --filter active=true
```

Each filter is passed directly to `NuvoloClient.search_devices`, enabling flexible queries without hard-coded organisation-specific fields.

## Development notes

- The repository intentionally avoids bundling any private or production-specific data. Ensure that you keep your `.env` file out of version control.
- The included `openapi.json` file documents the Claroty xDome API and can be imported into tools such as Postman for exploration.

## Troubleshooting

- A `ValueError` during client initialisation indicates that one or more required environment variables are missing.
- For network-related errors, verify firewall rules and confirm that the API credentials have the necessary permissions.

## License

This project is distributed for internal integration purposes. Adapt it to your organisation's policies before use in production.
