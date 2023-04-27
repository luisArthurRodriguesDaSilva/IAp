import os
import openai
from . import scrapeMe as sc
from .helpers import getText

openai_key = getText(os.path.join(os.getcwd(), "api_key.txt"))
openai.api_key = openai_key


final_text = "baseado nisso,"


def send_to_chatGPT(message):

    messages = sc.scrap_sistem()
    messages.append(
        {"role": "user", "content": final_text + message},
    )
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply
