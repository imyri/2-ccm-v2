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
        self.db_root = "Db"
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

    def call_gemini(self, prompt, system_instruction="You are a helpful assistant."):
        """Call Gemini API using the free-tier key."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.logger.error("GEMINI_API_KEY not found in .env")
            return "Error: No API Key."
            
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)
        
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            self.logger.error(f"Gemini API Error: {str(e)}")
            return f"Error: {str(e)}"

# Example usage pattern:
# if __name__ == "__main__":
#     module = CCMModule("BaseModule", "00-System")
#     module.logger.info("CCM Module Core Initialized.")
