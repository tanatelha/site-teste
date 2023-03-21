import os   # para acessar as variáveis de ambiente

import requests
from flask import Flask
from tchan import ChannelScraper

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"] #biblioteca para ver chaves
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]

app = Flask(__name__)

def ultimas_promocoes():
  scraper = ChannelScraper()
  contador = 0
  resultado = []
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    if contador == 10:
      return resultado

menu = """
<a href="/">Página inicial</a> | <a href="/promocoes">Promoções</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu + "<br> <br> Olá, mundo! Esse é o meu site. <br> <br> Quer saber um pouco mais sobre mim? Clique no 'Sobre' no topo da página"

@app.route("/sobre")
def sobre():
  return menu + "<br> <br> Você está na página Sobre! <br> <br> Se você está aqui, é porque você quer saber mais sobre mim. Para isso, vamos nos conhecer? Se quiser me conhecer, aperte em 'Contato' no topo da tela"

@app.route("/contato")
def contato():
  return menu + "<br> Para entrar em contato com a desenvolvedora desse site basta fazer sinal de fumaça ;)"

@app.route("/promocoes")
def promocoes():
  conteudo = menu + """
  Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos">@promocoeseachadinhos</a>:
  <br>
  <ul>
  """
  for promocoes in ultimas_promocoes():
    conteudo += f"<li>{promocao}</li>"
  return conteudo + "</ul>"


@app.route("/dedoduro")
def dedoduro():
  mensagem = {"chad_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem)
  return "Mensagem enviada."
  
