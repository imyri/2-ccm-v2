import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

class N8NHandler:
    """Handles communication between CCM and n8n automation engine."""
    
    def __init__(self):
        self.webhook_url = os.getenv("N8N_HITL_WEBHOOK_URL")
        self.enabled = os.getenv("HITL_ENABLED", "false").lower() == "true"
        
    def send_approval_request(self, niche, script_path, content, approval_endpoint):
        """Sends a script to n8n for human-in-the-loop approval."""
        if not self.enabled or not self.webhook_url:
            logging.info("n8n HITL is disabled or webhook URL is missing. Skipping approval request.")
            return False
            
        payload = {
            "event": "script_ready",
            "niche": niche,
            "script_path": script_path,
            "content": content,
            "approval_url": approval_endpoint,
            "timestamp": logging.Formatter("%(asctime)s").format(logging.LogRecord("", 0, "", 0, "", (), None))
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            logging.info(f"Successfully sent approval request to n8n for niche: {niche}")
            return True
        except Exception as e:
            logging.error(f"Failed to send webhook to n8n: {str(e)}")
            return False

    def notify_event(self, event_name, data):
        """Generic notification sender for n8n workflows."""
        if not self.webhook_url:
            return False
            
        payload = {
            "event": event_name,
            "data": data
        }
        
        try:
            requests.post(self.webhook_url, json=payload, timeout=5)
            return True
        except Exception:
            return False

if __name__ == "__main__":
    # Test (requires N8N_HITL_WEBHOOK_URL in .env)
    handler = N8NHandler()
    print(f"n8n Handler initialized. Enabled: {handler.enabled}")
