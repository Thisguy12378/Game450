from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
import json

import random
from util.llm_utils import run_console_chat, tool_tracker

Characterjson = Path(__file__).parent / "Character.json"
Creatorjson = Path(__file__).parent / "CharacterCreator.json"

def loadCharacterData(filePath):
    try:
        with open(filePath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading character data: {e}")
        return None

def saveCharacterData(filePath, data):
    try:
        with open(filePath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving character data: {e}")

def CreateCharacter():
    response = run_console_chat(Creatorjson, end_regex=r'CHARACTER CREATED')

    try:
        character = json.loads(response)
    except json.JSONDecodeError:
        print("Error decoding JSON response")

    saveCharacterData(Characterjson, character)

if __name__ == "__main__":
    CreateCharacter()
