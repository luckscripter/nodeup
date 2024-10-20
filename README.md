# Node Monitor Script

This Python script monitors your blockchain node (or any other service) and automatically restarts it if it goes down. It is designed for use on Linux systems running with `systemd`.

## Features
- **Node Status Monitoring**: The script checks whether your node (or service) is active using `systemctl`.
- **Automatic Restart**: If the node is found to be inactive, it automatically restarts the service.
- **Customizable**: You can configure the script to monitor any service by modifying the service name and path.

## Prerequisites
- Python 3.x installed on your server
- `systemctl` available for controlling services (Linux systems)
- Appropriate permissions to restart services via `systemctl` (you may need to run this script as a root or with `sudo`).

## How to Use

1. **Clone the repository** (or download the `node_monitor.py` script).

   ```bash
   git clone https://github.com/yourusername/node-monitor.git
   cd node-monitor
