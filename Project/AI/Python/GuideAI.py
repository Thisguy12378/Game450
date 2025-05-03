from util.llm_utils import run_console_chat, tool_tracker
from pathlib import Path

GuideAI = Path(__file__).parent / "dungeonMaster.json"

def runGuideAI(user_input):
    response = run_console_chat(template_file=GuideAI, user_input=user_input)
    return response