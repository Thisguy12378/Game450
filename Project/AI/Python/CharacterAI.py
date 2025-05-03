from util.llm_utils import run_console_chat, tool_tracker
from pathlib import Path
from Character import Character

CharacterAI = Path(__file__).parent / "CharacterUpdaterAI.json"

def runCharacterAI(user_input):
    response = run_console_chat(template_file=CharacterAI, user_input=user_input)
    return response

@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def updateCharacter(stat, value):
    Character.updateStat(stat, value)

def showCharacter():
    return Character.display_character()

def equipItem(item):
    Character.equipItem(item)

def unequipItem(item):
    Character.unequipItem(item)

def viewInventory():
    Character.displayInventory()

def viewEquipment():
    Character.displayEquipment()

def removeItem(item):
    Character.removeFromInventory(item)

def addItem(item):
    Character.addToInventory(item)