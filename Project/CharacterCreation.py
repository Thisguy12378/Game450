import ollama
import json
import requests

OLLAMA_URL = "http://localhost:11434/chat"

def loadPrompt(filePath):
    try:
        with open(filePath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading prompt: {e}")
        return None
    
def chat(payload):
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()

def main():
    prompt_data = loadPrompt("Project/CharacterCreator.json")
    messages = prompt_data["messages"]

    while True:
        userinput = input("You: ")
        messages.append({"role": "user", "content": userinput})

        payload = {"model" : prompt_data["model"],
                   "options" : prompt_data["options"],
                   "messages" : messages}

        response = chat(payload)
        ai_message = response['message']['content']
        messages.append({"role": "assistant", "content": ai_message})

        print(f"\nAI: {ai_message}\n")

        if "character sheet" in ai_message.lower() or "start the adventure" in ai_message.lower():
            break 

    with open("Character.json", "w") as f:
        json.dump(messages, f, indent=4)

if __name__ == "__main__":
    main()




        