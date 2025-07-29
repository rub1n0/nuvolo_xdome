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

3. Run the Claroty client example:
   ```bash
   python Claroty_Client.py
   ```

If the required variables are missing, the client will raise a `ValueError` explaining what is needed.
