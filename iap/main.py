import sys
from .helpers import save_on, getCode, getToken, setToken
from .iaApi import send_to_chatGPT, final_text


def main():
    final_file = 'chat.py'
    if len(sys.argv) > 1:
        final_file = sys.argv[1]

    if not getToken():
        setToken()

    prompt = input(f"Digite o prompt: \n{final_text}")

    try:
        reply = send_to_chatGPT(prompt)
        save_on('chat.txt', reply)
        code = getCode(reply)
        save_on(final_file, code)
    except Exception as e:
        print(e)
