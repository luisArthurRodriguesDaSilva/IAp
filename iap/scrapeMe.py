import os
from .helpers import getArg

curr_path = os.getcwd()
initial_text = "chat gpt, saiba que:\n"

def scrap_sistem():
    extension = getArg(1,'a.py').split('.')[-1]
    messages = [{"role": "system", "content": initial_text}]
    files_info_text = ""
    for dirpath, dirnames, filenames in os.walk(curr_path):
        for filename in filenames:
            if  filename.endswith(getArg(2,f".{extension}")):
                path_name= f"{'/'.join(dirpath.split('/')[-2:])}/{filename}"
                print(path_name, 'lido')
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r") as arquivo:
                        conteudo = arquivo.read()
                        curr_text = f"""
```python
O arquivo {path_name} contém:

{conteudo}
```

"""
                        messages.append(
                            {"role": "user", "content": curr_text},
                        )
                        files_info_text += curr_text
                except Exception as e:
                    print(e)

    complete_text = initial_text + files_info_text
    with open("test.txt", "w") as arquivo:
        arquivo.write(complete_text)
    return messages
