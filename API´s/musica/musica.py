from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        'Banda': 'Evanescence',
        'Música': 'Bring me to Life'
    },
    {
        'Banda': 'Avenged Sevenfold',
        'Música': 'Hail to The King'
    },
    {
        'Banda': 'Green Day',
        'Música': 'Boulevard of Broken Dreams'
    },
    {
        'Banda': 'Skillet',
        'Música': 'The Resistance'
    }
]

@app.route('/')
def obter_musicas():
    return jsonify(musicas)

# Metodo Get com Id - htpp://localhost:5555/musicas/1
@app.route('/musicas/<int:indice>')
def obter_musica(indice):
    return jsonify(musicas[indice])

# Metodo POST - adicionar musica - http://localhost:5555/musicas
@app.route('/musicas', methods=['POST'])
def postar_musica():
    musica = request.get_json()
    musicas.append(musica)

    return jsonify(musicas, 200)

# Metodo PUT = editar uma musica - http://localhost:5555/musicas/0
@app.route('/musicas/<int:indice>', methods=['PUT'])
def editar_musica(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)

    return jsonify(musicas[indice], 200)

# Metodo DELETE - Deletar musica = http://localhost:5555/musicas/0
@app.route('/musicas/<int:indice>', methods=['DELETE'])
def deletar_musica(indice):
    if musicas[indice] is not None:
        del musicas[indice]
        return jsonify('A musica foi excluída com sucesso.', 200)
    return jsonify('Música não encontrada.', 404)


app.run(port=5555, host='localhost', debug=True)
