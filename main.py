from flask import Flask, jsonify, request
app = Flask(__name__)

livros = [
  {
      'id' : 1,
      'titulo' : 'O Senhor dos Anéis - As Torres Gemias',
      'autor' : 'J.R.R Tolkien'
  },

  {
   'id' : 2,
      'titulo' : 'Harry Potter e a camara secreta',
      'autor' : 'J.K Howling' 
  },

  {
    'id' : 3,
      'titulo' : 'O Pequeno Princepe',
      'autor' : 'Antoine de Saint-Exupéry '
  },
]

#Consultar
@app.route('/livros',methods[GET])
def obter_livros():
    return jsonify(livros)

#consultarID
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

