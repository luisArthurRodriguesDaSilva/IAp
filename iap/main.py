from .helpers import save_on, getPyCode, getToken, setToken
from .iaApi import send_to_chatGPT, final_text


def main():
    if not getToken():
        setToken()

    prompt = input(f"Digite o prompt: \n{final_text}")
    try:
        reply = send_to_chatGPT(prompt)
        save_on("chat.txt", reply)
        code = getPyCode(reply)
        save_on("chat.py", code)
    except Exception as e:
        print(e)
