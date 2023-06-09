import os
import sys

def getArg(n, defaultValue=''):
    if len(sys.argv) > n:
        return sys.argv[n]
    return defaultValue

def getFlags():
    return list(filter(lambda x: x[:2] == '--',sys.argv))

def getFlagsDict():
    args = sys.argv
    flags = getFlags()
    group = dict()
    for i , flag in enumerate(flags):
        flagName = flag.replace('--','')
        start = args.index(flag)+1
        end = (len(args) + 1) if i == (len(flags)-1) else args.index(flags[i+1])
        collection = args[start:end]
        group[flagName] = []
        group[flagName] += collection
    return group

def save_on(path, data):
    with open(path, "w") as arquivo:
        arquivo.write(data)


def getPyCode(text):
    return text.split("```python")[1].split("```")[0]

def getCode(text):
    start = text.find("```")
    end = text.rfind("```", start + 3)
    code_block = text[start:end]
    without_firsth_line = "\n".join(code_block.split("\n")[1:])
    return without_firsth_line

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

#save_on('chat.py',getCode(getText('chat.txt'))) tests
