import json
from datetime import datetime
from config import AUDIT_LOG_PATH

def log_event(filename, contract_type):
    log = {
        "file": filename,
        "contract_type": contract_type,
        "timestamp": str(datetime.now())
    }

    try:
        with open(AUDIT_LOG_PATH, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(log)

    with open(AUDIT_LOG_PATH, "w") as f:
        json.dump(data, f, indent=4)
