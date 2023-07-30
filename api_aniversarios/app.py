from flask import Flask, jsonify, request

app = Flask(__name__)

aniversarios = [
    {
        'id': 1,
        'Name': 'Teste1',
        'date': '03-09-1997'
    },
    {
        'id': 2,
        'Name': 'teste2',
        'date': '02-05-2001'
    },
    {
        'id': 3,
        'Name': 'Iris Mariano Silva',
        'date': '02-06-2021'
    },
]

# Consultar todos


@app.route('/aniversarios', methods=['GET'])
def obter_aniversarios():
    return jsonify(aniversarios)


# Consultar por id
@app.route('/aniversarios/<int:id>', methods=['GET'])
def Obter_aniversario_id(id):
    for aniversario in aniversarios:
        if aniversario.get('id') == id:
            return jsonify(aniversario)


# Editar aniversário por id
@app.route('/aniversarios/<int:id>', methods=['PUT'])
def editar_aniversario_id(id):
    aniversario_alterado = request.get_json()
    for indice, aniver in enumerate(aniversarios):
        if aniver.get('id') == id:
            aniversarios[indice].update(aniversario_alterado)
            return jsonify(aniversarios[indice])


# Criar aniversario
@app.route('/aniversarios', methods=['POST'])
def incluir_aniversario():
    novo_aniversario = request.get_json()
    aniversarios.append(novo_aniversario)

    return jsonify(aniversarios)


# Deletar aniversario
@app.route('/aniversarios/<int:id>', methods=['DELETE'])
def deletar_aniversario(id):
    for indice, aniver in enumerate(aniversarios):
        if aniver.get('id') == id:
            del aniversarios[indice]

    return jsonify(aniversarios)


app.run(port=5000, host='localhost', debug=True)
