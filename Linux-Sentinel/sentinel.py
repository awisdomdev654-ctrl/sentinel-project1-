
import subprocess
import json
import time
from datetime import datetime

TRUSTED_IPS = ['127.0.0.1', '0.0.0.0', '::1']


def scan_system():
    login_check = subprocess.run(['last', '-n', '5'], capture_output=True, text=True).stdout
    # Insert this as the new Line 12
    connections = subprocess.run(['netstat', '-an'], capture_output=True, text=True).stdout
    # 2. STATUS LOGIC

    alerts = []
    status = "Secure"

    report = {
        "last_scan": datetime.now().strftime("%H:%M:%S"),
        "status": status,
        "alerts": alerts,
        "recent_logins": login_check.split('\n')[0] if login_check else "No recent logins"
    }

    with open('security_data.json', 'w') as f:
        json.dump(report, f, indent=4)

    print(f"[{report['last_scan']}] System {status}. Data exported to security_data.json")


if __name__ == "__main__":
    print("Sentinel Active... Monitoring Linux System.")
    while True:
        scan_system()
        time.sleep(60)
