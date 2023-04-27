def save_on(path, data):
    with open(path, "w") as arquivo:
        arquivo.write(data)


def getPyCode(text):
    return text.split("```python")[1].split("```")[0]


def getText(file):
    with open(file, "r") as arquivo:
        return arquivo.read()
