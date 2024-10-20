import subprocess
import time
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Node parameters
NODE_PATH = "/path/to/your/node/executable"
NODE_STATUS_CMD = "systemctl is-active your-node-service"  # Example command to check node status

# Function to check node status
def check_node_status():
    try:
        result = subprocess.run(NODE_STATUS_CMD, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip() == 'active'
    except subprocess.CalledProcessError:
        return False

# Function to restart the node
def restart_node():
    try:
        logger.info("Node is down. Restarting...")
        subprocess.run(f"systemctl restart your-node-service", shell=True, check=True)
        logger.info("Node restarted successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to restart node: {e}")

# Function to monitor the node
def monitor_node():
    while True:
        if not check_node_status():
            logger.warning("Node is down!")
            restart_node()
        else:
            logger.info("Node is running smoothly.")
        
        # Pause before the next check (e.g., 60 seconds)
        time.sleep(60)

if __name__ == "__main__":
    logger.info("Starting node monitor...")
    monitor_node()
