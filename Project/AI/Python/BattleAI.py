from util.llm_utils import run_console_chat, tool_tracker
from pathlib import Path
import json
import random


BattleAI = Path(__file__).parent / "BattleAI.json"
ENEMY_DATA = Path(__file__).parent / "ManagementJsons" / "Enemies.txt"

def runBattleAI(user_input):
    response = run_console_chat(template_file=BattleAI, user_input=user_input)
    return response

@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def getEnemy():
    try:
        with open(ENEMY_DATA, 'r') as f:
            content = f.read()

            enemies = content.split("##")[1:]
            if not enemies:
                print("No enemies found in the file.")
                return None

            enemy = random.choice(enemies).strip()

            lines = enemy.split("\n")
            name = lines[0].strip()
            description = lines[1].strip()
            health = (int(lines[2].split(":")[1].strip()))
            damage = (int(lines[3].split(":")[1].strip()))

            return {
                "name" : name,
                "description" : description,
                "health" : health,
                "damage" : damage
            }
    except FileNotFoundError:
        print(f"File {ENEMY_DATA} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

            