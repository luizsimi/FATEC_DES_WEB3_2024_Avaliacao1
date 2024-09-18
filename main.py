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












