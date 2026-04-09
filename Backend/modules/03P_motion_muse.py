import sys
import os
import importlib
import json

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class MotionMuse(CCMModule):
    def __init__(self):
        super().__init__("MotionMuse")

    def generate_shot_list(self, script_path):
        """Transform a script into a structured visual shot list."""
        self.logger.info(f"Generating shot list for script: {script_path}")
        
        if not os.path.exists(script_path):
            self.logger.error("Script file not found.")
            return None
            
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
            
        prompt = f"""
        SOCIAL MEDIA SCRIPT:
        {script_content}
        
        TASK:
        Break this script into a structured visual shot list for production.
        Each scene must have:
        1. scene_id: Incremental number.
        2. visual_prompt: A high-detail prompt for an AI image generator (Sleek Dark Mode Tech style).
        3. text_overlay: The short text to appear on screen.
        4. audio_cue: The script lines for this specific shot.
        
        Return ONLY a JSON array of objects.
        """
        
        system_instruction = "You are an expert Content Producer and Art Director."
        
        shot_list_raw = self.call_gemini(prompt, system_instruction=system_instruction)
        
        if "Error" in shot_list_raw:
            return shot_list_raw
            
        # Try to parse JSON from response
        try:
            # Clean possible markdown formatting
            clean_json = shot_list_raw.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json.replace("```json", "").replace("```", "").strip()
            elif clean_json.startswith("```"):
                clean_json = clean_json.replace("```", "").strip()
                
            shot_data = json.loads(clean_json)
            
            script_name = os.path.basename(script_path).replace("02N_script_", "").replace(".md", "")
            filename = f"03P_shot_list_{script_name}.json"
            filepath = self.save_output("Shots", filename, shot_data)
            
            return filepath
        except Exception as e:
            self.logger.error(f"Failed to parse Shot List JSON: {str(e)}")
            # Save raw as backup
            self.save_output("Shots", f"RAW_shot_list_{datetime.now().strftime('%H%M')}.json", {"raw": shot_list_raw})
            return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 03P_motion_muse.py <script_path>")
        sys.exit(1)
        
    script = sys.argv[1]
    muse = MotionMuse()
    result = muse.generate_shot_list(script)
    print(f"Shot list result: {result}")
