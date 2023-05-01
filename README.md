# IAp

O IAp é um projeto que integra a plataforma OpenAI GPT-3 a um ambiente local do usuário, facilitando a criação de arquivos que seriam repetitivos mas exigissem um contexto maior da aplicação

## Instalação

O pacote pode ser instalado via pip, utilizando o seguinte comando:
```bash
pip install auto-iap-enviroment
```

## Como utilizar

Para utilizar o IAp, digite o seguinte comando no terminal:
```bash
iap [CAMINHO_ARQUIVO.py] [EXTENÇÃO_MONITORADA]
```
Onde `[CAMINHO_ARQUIVO]` é um caminho absoluto para o arquivo em que você deseja salvar a resposta gerada pelo GPT-3 e `[EXTENÇÃO_MONITORADA]` é o tipo de arquivo vigiado pelo IAp

> Detalhe que  valor default de `[EXTENÇÃO_MONITORADA]` é a extenção de `[CAMINHO_ARQUIVO]`

Após a execução do comando, você deverá digitar o prompt que deseja enviar para o GPT-3.

A partir disso o IAp treinara o GPT-3 com todos os arquivos que contenham a extenção monitorada para que ele entenda o contexto do seu projéto e, dessa maneira, retornando uma melhor resposta, que é salva no arquivo especificado anteriormente.

Comandos adicionais disponíveis:

- `iap setToken`:  Realiza a mudança do token openai que será utilizado pela api no funcionamento.

## Exemplo de utilização

lendo todos os .py e escrevendo o código em exemplo.py

```bash
iap exemplo.py 
```

lendo todos os .js e escrevendo o código em exemplo.py

```bash
iap exemplo_dois.py js
```

## Video do funcionamento

https://user-images.githubusercontent.com/66787949/235394544-02f41fd5-d7d2-4cba-bf2c-5ab26a9fdfed.mp4



O usuário digita um prompt no terminal e o IAp envia, junto com as informações dos arquivos, esse prompt para o GPT-3. O GPT-3 gera uma resposta, que é enviada de volta para o IAp, que salva no arquivo especificado pelo usuário.

## Dependências

- openai (1.10.0)
- setuptools (57.4.0)

## Desenvolvimento

O projeto pode ser encontrado em [https://github.com/luisArthurRodriguesDaSilva/IAp/tree/main](https://github.com/luisArthurRodriguesDaSilva/IAp/tree/main). Qualquer sugestão ou contribuição é bem-vinda! 
