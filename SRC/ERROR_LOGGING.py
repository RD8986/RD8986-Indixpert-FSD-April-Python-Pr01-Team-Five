import json
import os
from datetime import datetime

LOG_FILE = os.path.join('database', 'exception_log.json')

def log_error(message):
    error_entry = {
        "timestamp": datetime.now().isoformat(),
        "error": message
    }
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)

    with open(LOG_FILE, 'r+') as f:
        logs = json.load(f)
        logs.append(error_entry)
        f.seek(0)
        json.dump(logs, f, indent=4)
