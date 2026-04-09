import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

# Initialize environment
load_dotenv()

class CCMModule:
    """Base class for all CCM deterministic modules (M)."""
    
    def __init__(self, name):
        self.name = name
        # Find project root (where .env usually lives)
        self.project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.db_root = os.path.join(self.project_root, "Db")
        self.backend_root = os.path.join(self.project_root, "Backend")
        self.setup_logging()
        
    def setup_logging(self):
        log_dir = os.path.join(self.db_root, "Logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"{self.name}_{datetime.now().strftime('%Y%m%d')}.log")
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.name)

    def save_output(self, folder, filename, data):
        """Standard method to save output (JSON or Markdown) to the Db vault."""
        target_dir = os.path.join(self.db_root, folder)
        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, filename)
        
        if filename.endswith(".json"):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(data))
                
        self.logger.info(f"Output saved to {filepath}")
        return filepath

    def call_gemini(self, prompt, system_instruction="You are a helpful assistant.", retries=3, backoff=5):
        """Call Gemini API with retries and exponential backoff using the new google-genai SDK."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.logger.error("GEMINI_API_KEY not found in .env")
            return "Error: No API Key."
            
        from google import genai
        import time
        
        # Initialize the new Client
        client = genai.Client(api_key=api_key)
        
        # Using gemini-2.0-flash for state-of-the-art performance and quotas
        model_id = 'gemini-2.0-flash'
        
        for attempt in range(retries):
            try:
                # New Client-based generation
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        system_instruction=system_instruction
                    )
                )
                return response.text
            except Exception as e:
                # Handle quota and general errors
                err_str = str(e)
                if "429" in err_str or "ResourceExhausted" in err_str:
                    wait_time = backoff * (2 ** attempt)
                    self.logger.warning(f"Quota exceeded (429). Retrying in {wait_time}s... (Attempt {attempt+1}/{retries})")
                    time.sleep(wait_time)
                else:
                    self.logger.error(f"Gemini API Error: {err_str}")
                    return f"Error: {err_str}"
        
        return "Error: Max retries exceeded for Gemini API call."

# Example usage pattern:
# if __name__ == "__main__":
#     module = CCMModule("BaseModule", "00-System")
#     module.logger.info("CCM Module Core Initialized.")
