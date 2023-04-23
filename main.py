import os

curr_path = os.getcwd()
initial_text = "chat gpt, saiba que\n"
final_text = "me escreva o código que faça \n"


def main():

    prompt = input("Digite o prompt: ")
    files_info_text = ""
    for dirpath, dirnames, filenames in os.walk(curr_path):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r") as arquivo:
                    conteudo = arquivo.read()
                    curr_text = f"""
```python
O arquivo {file_path} contém:

{conteudo}
```

"""
                    print(curr_text)
                    files_info_text += curr_text

    complete_text = initial_text + files_info_text + final_text + prompt
    with open("test.txt", "w") as arquivo:
        arquivo.write(complete_text)


main()
