import os

global_path = "/".join(os.getcwd().split("/")[:3])
token_path = os.path.join(global_path, "iap_token.txt")


def save_on(path, data):
    with open(path, "w") as arquivo:
        arquivo.write(data)


def get_py_code(text):
    return text.split("```python")[1].split("```")[0]


def get_code(text):
    start = text.find("```")
    end = text.find("```", start + 3)
    code_block = text[start:end]
    without_firsth_line = "\n".join(code_block.split("\n")[1:])
    return without_firsth_line


def get_text(file):
    try:
        with open(file, "r") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return ""


def get_token():
    return get_text(token_path)


def set_token():
    token = input("token: ")
    save_on(token_path, token)
    return token


save_on("chat1.txt", get_code(get_text("chat.txt")))
