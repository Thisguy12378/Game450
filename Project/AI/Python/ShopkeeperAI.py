from util.llm_utils import run_console_chat, tool_tracker
from pathlib import Path
from Character import Character
import json

ShopkeeperAI = Path(__file__).parent / "ShopkeeperAI.json"
shopInventory = Path(__file__).parent / "ManagementJsons" / "ShopInventory.json"

def runShopkeeperAI(user_input):
    response = run_console_chat(template_file=ShopkeeperAI, user_input=user_input)
    return response

@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def addToInventory(item):
    Character.addToInventory(item)

def loadShopInventory():
    try:
        with open(shopInventory, 'r') as f:
            inventory = json.load(f)["shops"]
            return inventory
    except FileNotFoundError:
        print(f"File {shopInventory} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {shopInventory}.")
        return None