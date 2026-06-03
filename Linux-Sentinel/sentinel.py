import subprocess
import json
import time
from datetime import datetime

TRUSTED_IPS = ['127.0.0.1', '0.0.0.0', '::1']

def scan_system():
    # 1. Capture system telemetry
    login_check = subprocess.run(['last', '-n', '5'], capture_output=True, text=True).stdout
    connections = subprocess.run(['netstat', '-an'], capture_output=True, text=True).stdout

    alerts = []
    status = "Secure"

    # 2. PARSING LOGIC: Scan active network connections line-by-line
    for line in connections.split('\n'):
        # We look for lines containing 'ESTABLISHED' or active connection states
        if 'ESTABLISHED' in line or 'LISTEN' in line:
            parts = line.split()
            if len(parts) >= 5:
                # Extract the foreign address column (usually the 5th item)
                foreign_addr = parts[4]
                
                # Strip out port numbers to isolate just the IP address
                remote_ip = foreign_addr.rsplit(':', 1)[0].split('.')[-1] if ':' in foreign_addr else foreign_addr
                
                # Check if this IP is a potential intruder
                # Check if this IP is an actual external intruder
                is_local = any(trusted in remote_ip for trusted in TRUSTED_IPS) or remote_ip in ['*', '*.*', '0', '']

                if not is_local:
                    alerts.append(f"Unrecognized active connection detected from: {foreign_addr}")
                    status = "Warning"
    # 3. Compile the JSON Telemetry Report
    report = {
        "last_scan": datetime.now().strftime("%H:%M:%S"),
        "status": status,
        "alerts": alerts,
        "recent_logins": login_check.split('\n')[0] if login_check else "No recent logins"
    }

    # 4. Export for the frontend DOM to consume
    with open('security_data.json', 'w') as f:
        json.dump(report, f, indent=4)

    print(f"[{report['last_scan']}] System {status}. Active Alerts: {len(alerts)}. Data exported.")

if __name__ == "__main__":
    print("Sentinel Active... Monitoring Linux System.")
    while True:
        scan_system()
        time.sleep(10) # Scanning every 10 seconds for snappy testing