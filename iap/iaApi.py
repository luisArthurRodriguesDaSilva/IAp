import openai
from . import scrapeMe as sc
from .helpers import getText, getToken



final_text = "baseado nisso,"


def send_to_chatGPT(message):

    openai_key = getToken()
    openai.api_key = openai_key

    messages = sc.scrap_sistem()
    messages.append(
        {"role": "user", "content": final_text + message},
    )
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply
