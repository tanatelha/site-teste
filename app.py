from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Esse é o meu site. <br> <br> Quer saber um pouco mais sobre mim? Clique no 'Sobre' no topo da página"

@app.route("/sobre")
def sobre():
  return menu + "Você está na página Sobre! <br> <br> Se você está aqui, é porque você quer saber mais sobre mim. Para isso, vamos nos conhecer? Se quiser me conhecer, aperte em 'Contato' no topo da tela"

@app.route("/contato")
def contato():
  return menu + "Para entrar em contato com a desenvolvedora desse site basta fazer sinal de fumaça"

