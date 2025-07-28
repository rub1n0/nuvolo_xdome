import os
import nuvolo_cmms_client
from dotenv import load_dotenv

load_dotenv()

nuvolo = nuvolo_cmms_client.NuvoloCMMSClient(
    instance_url=os.getenv("INSTANCE_NUVOLO"),
    username=os.getenv("USER_NUVOLO"),
    password=os.getenv("PASS_NUVOLO"),
    table=os.getenv("TABLE_NUVOLO")
)

nuvolo.get_record(
    sys_id="fd7c101cebcb6e10b8ceff47bad0cd99",
    sysparm_fields="name"
)
