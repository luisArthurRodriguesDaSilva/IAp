import dotenv
import os
import openai

dotenv.load_dotenv(dotenv.find_dotenv())

startOfPrompts = "day realistic, focused, older and modern"

openai_key = os.getenv("openaiApiKey")
openai.api_key = openai_key
print(openai_key)


messages = [{"role": "system", "content": "You are a intelligent assistant."}]

chat = openai.ChatCompletion.create(model="ada", messages=messages)

message = 'what is your name?'
messages.append(
    {"role": "user", "content": message},
)


reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")
