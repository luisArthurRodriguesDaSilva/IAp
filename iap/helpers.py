import os


def save_on(path, data):
    with open(path, "w") as arquivo:
        arquivo.write(data)


def getPyCode(text):
    return text.split("```python")[1].split("```")[0]


def getText(file):
    try:
        with open(file, "r") as arquivo:
            return arquivo.read()
    except Exception:
        with open(file, "w") as arquivo:
            arquivo.write("")
        return getText(file)


global_path = "/".join(os.getcwd().split("/")[:3])
token_path = global_path + "/iap_token.txt"


def getToken():
    token = getText(token_path)
    return token


def setToken():
    token = input("token: ")
    save_on(token_path, token)
    return token
