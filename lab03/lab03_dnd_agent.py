from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Collin Miller'
model = 'llama3.2'
options = {'Temperature': .5, 'max_tokens' : 75}
messages = [{'role': 'system', 'content': 'I want you to be evil and be very unsure of yourself and speak like it is medieval times'},]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

  # Add your code below
  message = {'role' : 'user', 'content' : input("You: ")}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

