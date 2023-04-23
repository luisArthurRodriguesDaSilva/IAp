import os

curr_path = os.getcwd()


def main():
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

{conteudo}```

"""
                    print(curr_text)
                    files_info_text += curr_text

    with open("super.txt", "w") as f:
        f.write(files_info_text)
