# nuvolo_xdome

This repository contains simple clients for interacting with Claroty xDome and Nuvolo CMMS APIs. The clients rely on a few environment variables for configuration.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file based on `.env.example` and populate it with your API credentials.
   Required variables for `Claroty_Client`:
   - `CLAROTY_BASE_URL` – Base URL of the Claroty xDome instance.
   - `CLAROTY_API_KEY` – API token for authentication.

   Required variables for `NuvoloCMMSClient`:
   - `NUVOLO_INSTANCE` – Base URL to your Nuvolo instance.
   - `NUVOLO_DEVICES_TABLE` – Path to the devices table.
   - `NUVOLO_USER` – Username for authentication.
   - `NUVOLO_PASSWORD` – Password for authentication.

3. Run the Claroty client example:
   ```bash
   python Claroty_Client.py
   ```

4. Run the Nuvolo CMMS client example:
   ```bash
   python Nuvolo_Client.py
   ```

5. Run the matching engine to search xDome for devices whose `cmdb_asset_tag` matches the CMMS `name` field:
   ```bash
   python engine.py
   ```

If the required variables are missing, the client will raise a `ValueError` explaining what is needed.
