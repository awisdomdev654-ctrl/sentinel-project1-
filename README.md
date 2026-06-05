# Linux Sentinel Telemetry Dashboard 🛡️

A full-stack, real-time DevSecOps telemetry system that monitors active system connections, parses network socket states, and streams live security metrics to a responsive frontend web console.

## 🎥 Live Demo

(https://youtu.be/PuseKxssnQo)**

*Note: The system dashboard dynamically shifts from a secure cockpit to an active warning state in under 5 seconds when the backend automation engine flags unverified socket activity.*

---

## 🏗️ System Architecture

This project is decoupled into three primary layers, shifting security telemetry "left" by bringing infrastructure awareness straight into the developer interface.

1. **The Telemetry Engine (`sentinel.py`):** A backend Python engine that utilizes low-level system subprocesses to trace active network socket states. It parses open connections line-by-line, filters out safe loopback traffic based on a trusted IP whitelist, and flags unexpected external listeners.
2. **The Structured Data Contract (`security_data.json`):** A real-time data layer that decouples the backend infrastructure scanners from the client console, enabling scalable data ingestion.
3. **The Control Cockpit (`index.html`, `style.css`, `index-sentinel.js`):** An asynchronous vanilla JavaScript dashboard that constantly queries the local data pipeline, using smooth CSS state transitions and strict DOM manipulation to accurately report the system's defensive state.

---

## 🛠️ Technical Stack

- **Backend Logic:** Python 3 (Subprocess, JSON automation, Time-series loops)
- **Frontend Console:** HTML5, Vanilla CSS3 (Keyframes & pulsing alert transitions)
- **Data Pipeline:** JavaScript (Async/Fetch API, JSON data parsing, DOM Manipulation)
- **Development Tooling:** Warp Terminal, PyCharm / VS Code, Git Version Control

---

## 🚀 Local Installation & Deployment

To run this telemetry ecosystem locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Linux-Sentinel.git](https://github.com/YOUR_USERNAME/Linux-Sentinel.git)
cd Linux-Sentinel
