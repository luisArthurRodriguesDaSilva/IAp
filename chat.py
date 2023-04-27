import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import tweepy

# Define as informações da sua conta no Twitter
consumer_key = "SEU_CONSUMER_KEY"
consumer_secret = "SEU_CONSUMER_SECRET"
access_token = "SEU_ACCESS_TOKEN"
access_token_secret = "SEU_ACCESS_TOKEN_SECRET"

# Autentica na API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Caminho para o arquivo de texto com o código do programa
caminho_arquivo = "test.txt"

# Lê o conteúdo do arquivo
with open(caminho_arquivo, "r") as f:
    codigo = f.read()

# Define as configurações da imagem
largura_imagem = 800
altura_imagem = 800
fonte = ImageFont.truetype("arial.ttf", 16)
margem = 50
espacamento_linhas = 20
cor_fundo = (255, 255, 255)
cor_texto = (0, 0, 0)

# Cria a imagem
imagem = Image.new("RGB", (largura_imagem, altura_imagem), color=cor_fundo)
desenho = ImageDraw.Draw(imagem)

# Divide o código em linhas
linhas = codigo.split("\n")

# Escreve cada linha da imagem
posicao_y = margem
for linha in linhas:
    desenho.text((margem, posicao_y), linha, font=fonte, fill=cor_texto)
    posicao_y += espacamento_linhas

# Salva a imagem como um novo arquivo
imagem.save("codigo.png")

# Posta a imagem no Twitter
with open("codigo.png", "rb") as f:
    imagem_bytes = f.read()
    api.update_with_media(
        "codigo.png",
        file=BytesIO(imagem_bytes),
        status="Aqui está o código do programa que gerei usando a API de IA!",
    )
