from .helpers import save_on, getPyCode
from .iaApi import send_to_chatGPT, final_text


def main():
    prompt = input(f"Digite o prompt: \n{final_text}")
    reply = send_to_chatGPT(prompt)
    try:
        code = getPyCode(reply)
        print(reply)
        save_on("chat.py", code)
    except Exception as e:
        print(e)
        save_on("chat.txt", reply)
