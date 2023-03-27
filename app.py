# bibliotecas que já vem com python
import os   # para acessar as variáveis de ambiente

# bibliotecas externas: import em ordem alfabética e depois froms em ordem alfabética
import gspread
import requests
from flask import Flask
from oauth2client.service_account import ServiceAccountCredentials 
from tchan import ChannelScraper


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"] #biblioteca para ver chaves
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")

api = gspread.authorize(conta)
planilha = api.open_by_key('1ZDyxhXlCtCjMbyKvYmMt_8jAKN5JSoZ7x3MqlnoyzAM') # isso poderia estar em uma variável de ambiente
sheet = planilha.worksheet('Sheet1') # isso poderia estar em uma variável de ambiente


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
  mensagem = {"chat_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  resposta = requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem)
  return f"Mensagem enviada. Resposta ({resposta.status_code}): {resposta.text}"

@app.route("/dedoduro2")
def dedoduro2():
  sheet.append_row(["Natalia", "Santos", "a partir do Flask"])
  return "Planilha escrita!"
  
