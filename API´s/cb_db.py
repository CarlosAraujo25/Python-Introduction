from flask import Flask, jsonify, request, make_response
from estrutura_banco_de_Dados import  Autor, Postagem, app, db
import jwt
import json
from datetime import datetime, timedelta
from functools import wraps

# Rota padrão - GET http://localhost:5000

def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Verificar se um token foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'Mensagem':'Token não incluído'}, 401)
        # Se temos um token, validar acesso no banco de dados
        try:
           resultado = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256'])
           autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'Mensagem':'Token é inválido'}, 401)
        return f(autor, *args, **kwargs)
    return decorated


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    usuario = Autor.query.filter_by(nome=auth.username).first()
    if not usuario:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor':usuario.id_autor, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token})
    return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})

@app.route('/')
@token_obrigatorio
def obter_postagens(autor):
    postagens = Postagem.query.all()

    list_postagens = []
    for postagem in postagens:
        postagem_atual = {}
        postagem_atual['título'] = postagem.título
        postagem_atual['id_autor'] = postagem.id_autor
        list_postagens.append(postagem_atual)
    return jsonify({'postagens': list_postagens})

# GEt com Id http://localhost:5000/postagens/1
@app.route('/postagem/<int:id_postagem>', methods=['GET'])
@token_obrigatorio
def obter_postagem_por_indice(autor, id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    postagem_atual = {}
    try:
        postagem_atual['título'] = postagem.título
    except:
        pass
    postagem_atual['id_autor'] = postagem.id_autor
    
    return jsonify({'postagens': postagem_atual})

# Criar uma nova postagem - POST - http://localhost:5000/postagens
@app.route('/postagem', methods=['POST'])
@token_obrigatorio
def nova_postagem(autor):
    nova_postagem = request.get_json()
    postagem = Postagem(título=nova_postagem['título'], id_autor=nova_postagem['id_autor'])

    db.session.add(postagem)
    db.session.commit()

    return jsonify({'mensagem': 'Postagem criada com sucesso'}, 200)

# Alterar postagem existente - PUT - http://localhost:5000/postagens/0
@app.route('/postagem/<int:id_postagem>', methods=['PUT'])
@token_obrigatorio
def alterar_postagem(autor, id_autor, id_postagem):
    postagem_alterada = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    try:
        postagem.título = postagem_alterada['t´tiulo']
    except:
        pass
    try:
        postagem.id_autor = postagem_alterada['id_autor']
    except:
        pass
    
    db.session.commit()
    return jsonify({'Mensagem': 'Postagem alterada com sucesso.'})

# Excluindo postagem - DELETE - http://localhost:5000/postagens/0
@app.route('/postagens/<int:id_postagem>', methods=['DELETE'])
@token_obrigatorio
def excluir_postagem(autor, id_postagem):
    excluir_poostagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not excluir_poostagem:
        return jsonify({'Mensagem': 'Não foi possivel encontrar umma postagem com esse id.'})
    db.session.delete(excluir_poostagem)
    db.session.commit()

    return jsonify({'Mensagem': 'Postagem excluída com sucesso.'})
   

@app.route('/autores')
@token_obrigatorio
def obter_autores(autor):
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)

    return jsonify({'autores': lista_de_autores})


@app.route('/autores/<int:id_autor>', methods=['GET'])
@token_obrigatorio
def obter_autores_por_id(autor, id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor não encontrado!')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email

    return jsonify({'autor': autor_atual})

@app.route('/autores', methods=['POST'])
@token_obrigatorio
def novo_autor(autor):
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])

    db.session.add(autor)
    db.session.commit()

    return jsonify({'mensagem': 'Usúario criado com sucesso.'}, 200)

@app.route('/autores/<int:id_autor>', methods=['PUT'])
@token_obrigatorio
def alterar_autor(autor, id_autor):
    alterar_usuario = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    
    if not autor:
        return jsonify({'Mensagem': 'Este usúarios não foi encontrado.'})
    try:
        if alterar_usuario['nome']:
            autor.nome = alterar_usuario['nome']
    except:
        pass
    try:
        if alterar_usuario['emal']:
            autor.email = alterar_usuario['email']
    except:
        pass
    try:
        if alterar_usuario['senha']:
            autor.senha = alterar_usuario['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'Mensagem': 'Usúario não encontrado.'})

@app.route('/autores/<int:id_autor>', methods=['DELETE'])
@token_obrigatorio
def excluir_autor(autor, id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'Mensagem': 'Este usúario não foi econtrado.'})
    db.session.delete(autor_existente)
    db.session.commit()

    return jsonify({'Mensagem': 'Autor excluído com sucesso'}, 200)

app.run(port=5555, host='localhost', debug=True)
