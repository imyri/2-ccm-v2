import sys
import os
import importlib

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class ScriptSmith(CCMModule):
    def __init__(self):
        super().__init__("ScriptSmith")
        self.instructions_dir = os.path.join("Backend", "instructions")

    def load_instruction(self, filename):
        path = os.path.join(self.instructions_dir, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def generate_script(self, research_report_path, platform="ShortForm"):
        """Generate a viral script based on a research report."""
        self.logger.info(f"Generating script for report: {research_report_path}")
        
        if not os.path.exists(research_report_path):
            self.logger.error("Research report not found.")
            return None
            
        with open(research_report_path, 'r', encoding='utf-8') as f:
            report_content = f.read()
            
        sop = self.load_instruction("02N_scripting_sop.md")
        
        if platform == "ShortForm":
            template = self.load_instruction("02N_short_form_template.md")
        else:
            template = self.load_instruction("02N_thread_template.md")
            
        prompt = f"""
        RESEARCH REPORT:
        {report_content}
        
        SCRIPTING SOP:
        {sop}
        
        TEMPLATE:
        {template}
        
        TASK:
        Generate a high-authority, viral script based on the research report above. 
        Follow the SOP and TEMPLATE strictly. 
        Focus on the 'Pragmatic Architect' persona.
        """
        
        system_instruction = "You are an expert AI Scriptwriter for high-retention social media content."
        
        script_output = self.call_gemini(prompt, system_instruction=system_instruction)
        
        if "Error" in script_output:
            return script_output
            
        report_name = os.path.basename(research_report_path).replace("report_", "").replace(".md", "")
        filename = f"02N_script_{report_name}_{platform.lower()}.md"
        filepath = self.save_output("Scripts", filename, script_output)
        
        return filepath

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 02N_script_smith.py <report_path> [platform]")
        sys.exit(1)
        
    report = sys.argv[1]
    plat = sys.argv[2] if len(sys.argv) > 2 else "ShortForm"
    
    smith = ScriptSmith()
    result = smith.generate_script(report, platform=plat)
    print(f"Script generation result: {result}")
