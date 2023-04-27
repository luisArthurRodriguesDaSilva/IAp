import dotenv
import os
import openai
from helpers import save_on
import scrapeMe as sc

dotenv.load_dotenv(dotenv.find_dotenv())
openai_key = os.getenv("openaiApiKey")
openai.api_key = openai_key
print(openai_key)


final_text = "baseado nisso, me escreva o código que faça "
prompt = input("Digite o prompt: ")
complete_prompt = final_text + prompt

messages = sc.scrap_sistem()
messages.append(
    {"role": "user", "content": complete_prompt},
)


chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
reply = chat.choices[0].message.content


def send_to_chatGPT(message):
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply


print(f"ChatGPT: {reply}")
save_on("chat.txt", reply)
