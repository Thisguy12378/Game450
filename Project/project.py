from pathlib import Path
import sys
import json
from util.llm_utils import run_console_chat, tool_tracker
from Character import Character
from AI.Python.CharacterAI import runCharacterAI
from AI.Python.GuideAI import runGuideAI
from AI.Python.BattleAI import runBattleAI
from AI.Python.ShopkeeperAI import runShopkeeperAI

# Define paths to JSON files

def game_loop():
    """Main game loop to manage AI switching dynamically."""
    print("Welcome to the game!")
    current_ai = "GuideAI"  # Start with the Guide AI

    while True:
        if current_ai == "GuideAI":
            user_input = input("You: ")
            if user_input.lower() == "quit" or user_input.lower() == "exit":
                print("Exiting the game. Goodbye!")
                break

            guide_response = runGuideAI(user_input)
            print(f"Guide AI: {guide_response}")

            # Check for specific triggers in the Guide AI's response
            if "encounter an enemy" in guide_response.lower():
                print("Switching to Battle AI...")
                current_ai = "BattleAI"
            elif user_input.lower() == "shop":
                print("Switching to Shopkeeper AI...")
                current_ai = "ShopkeeperAI"
            elif user_input.lower() == "character":
                print("Switching to Character AI...")
                current_ai = "CharacterAI"

        elif current_ai == "BattleAI":
            user_input = input("You: ")
            if user_input.lower() == "back":
                print("Returning to Guide AI...")
                current_ai = "GuideAI"
                continue

            battle_response = runBattleAI(user_input)
            print(f"Battle AI: {battle_response}")

        elif current_ai == "ShopkeeperAI":
            user_input = input("You: ")
            if user_input.lower() == "back":
                print("Returning to Guide AI...")
                current_ai = "GuideAI"
                continue

            shop_response = runShopkeeperAI(user_input)
            print(f"Shopkeeper AI: {shop_response}")

        elif current_ai == "CharacterAI":
            user_input = input("You: ")
            if user_input.lower() == "back":
                print("Returning to Guide AI...")
                current_ai = "GuideAI"
                continue

            character_response = runCharacterAI(user_input)
            print(f"Character AI: {character_response}")

if __name__ == "__main__":
    game_loop()
