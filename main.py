#IMPORTAÇÃO DE BIBLIOTECA
from flask import Flask, render_template, request, redirect, session, flash, url_for
from dbparking import DbParking


class Jogo:
    #metodo construtor
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('SpiderMan', 'Acao', 'PS5')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS5')
lista = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Lennon Lima","lennlima","ll")
usuario2 = Usuario("Paola Santos","paollasantos","ll")
usuario3 = Usuario("Banco Dados","BD","ll")

usuarios = {usuario1.nickname : usuario1, 
            usuario2.nickname : usuario2, 
            usuario3.nickname : usuario3}

#instancia o Flask
app = Flask(__name__)
app.secret_key = '******'

@app.route('/')
def index():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect('/login')
    return render_template('lista.html', titulo="Jogos", jogos = lista)

@app.route('/novo')
def novo():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastro')

@app.route("/cadastrar")
def cadastrar():
      return render_template('cadastro.html', titulo='Cadastro')
    
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    usuario = request.form['usuario']
    senha = request.form['senha']
    adm = request.form['adm']
    db = DbParking()
    db.IncluirUsuario(usuario, nome, senha, adm)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Falha na autenticação!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


#não utilizar estas definições para produção, estas opções foram preparadas para ajudar no ambiente de desenvolvimento.
# app.run(host='127.0.0.1', port=8080)

#roda o flask / o debug=True vc pode salvar o projeto e ele atualiza sozinho o navegador, sem necessidade de fechar e rodar
app.run(debug=True)