# Documentação da API IAp

A API IAp é um projeto que integra a plataforma OpenAI GPT-3 a um ambiente local do usuário.

## Instalação

O pacote pode ser instalado via pip, utilizando o seguinte comando:
```bash
pip install git+https://github.com/luiarthur/auto-iap-enviroment.git
```

## Como utilizar

Para utilizar a API, digite o seguinte comando no terminal:
```bash
iap [CAMINHO_ARQUIVO.py]
```
Onde `[CAMINHO_ARQUIVO.py]` é um caminho absoluto para o arquivo em que você deseja salvar a resposta gerada pelo GPT-3.

Após a execução do comando, você deverá digitar o prompt que deseja enviar para o GPT-3. Ele irá gerar uma resposta, que será salva no arquivo especificado anteriormente.

Alguns comandos adicionais são disponíveis:

- `iap setToken`: define o token de acesso ao OpenAI. Este comando deve ser executado antes da utilização da API.

## Exemplo de utilização

```bash
iap /home/luis/exemplo.py
```

## Fluxo de funcionamento

O fluxo de funcionamento da API é mostrado abaixo:

![Fluxo de funcionamento](https://i.imgur.com/5a51cIu.png)

O usuário digita um prompt no terminal e a API envia este prompt para o GPT-3. O GPT-3 gera uma resposta, que é enviada de volta para a API e salva no arquivo especificado pelo usuário.

## Dependências

- openai (1.10.0)
- setuptools (57.4.0)

## Limitações conhecidas

A API consegue enviar cerca de 50 prompts por dia, devido às restrições do OpenAI GPT-3. Além disso, o token de acesso ao OpenAI deve ser gerado pelo próprio usuário.

## Desenvolvimento

O projeto pode ser encontrado em [https://github.com/luiarthur/auto-iap-enviroment](https://github.com/luiarthur/auto-iap-enviroment). Qualquer sugestão ou contribuição é bem-vinda! 

## Autor

Luis Arthur Rodrigues da Silva

## Licença

Este projeto segue os termos de licença do [MIT License](https://opensource.org/licenses/MIT).