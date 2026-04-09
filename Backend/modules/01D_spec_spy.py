import sys
import os
import json
import importlib
from datetime import datetime

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class SpecSpy(CCMModule):
    def __init__(self):
        super().__init__("SpecSpy")
        self.instructions_dir = os.path.join(self.backend_root, "instructions")

    def load_instruction(self, filename):
        path = os.path.join(self.instructions_dir, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def research_signal(self, signal_file_path):
        """Perform deep research on a specific trend signal."""
        self.logger.info(f"Performing deep research on signal: {signal_file_path}")
        
        if not os.path.exists(signal_file_path):
            self.logger.error("Signal file not found.")
            return None
            
        with open(signal_file_path, 'r', encoding='utf-8') as f:
            signals = json.load(f)
            
        if not signals or len(signals) == 0:
            self.logger.warning("No signals found in file.")
            return None
            
        # Prioritize the first signal (typically the hottest one)
        target = signals[0]
        
        template = self.load_instruction("01D_research_template.md")
        guide = self.load_instruction("01D_specs_guide.md")
        
        prompt = f"""
        TREND SIGNAL:
        {json.dumps(target, indent=2)}
        
        RESEARCH GUIDE:
        {guide}
        
        OUTPUT TEMPLATE:
        {template}
        
        TASK:
        Perform deep research on the tool or topic mentioned in the signal.
        Follow the RESEARCH GUIDE strictly. 
        Zero hallucinations. If a spec isn't found, mark as "N/A".
        Fill out the OUTPUT TEMPLATE completely.
        """
        
        system_instruction = "You are an expert Technical Researcher and Content Strategist. Your job is to verify specs and find factual alternatives."
        
        # Use our built-in Gemini call from CCMModule
        research_output = self.call_gemini(prompt, system_instruction=system_instruction)
        
        if "Error" in research_output:
            return research_output
            
        # Clean title for filename
        topic_name = "".join([c for c in target.get('title', 'Unknown') if c.isalnum() or c==' ']).strip().replace(" ", "_").lower()[:30]
        filename = f"report_{topic_name}_{datetime.now().strftime('%Y%m%d')}.md"
        filepath = self.save_output("Research", filename, research_output)
        
        return filepath

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 01D_spec_spy.py <signal_file_path>")
        sys.exit(1)
        
    sig_path = sys.argv[1]
    spy = SpecSpy()
    result = spy.research_signal(sig_path)
    print(f"Research result: {result}")
