from flask import jsonify
from app import app
from models import Consumidor


# Obtener todas las ordenes
@app.route('/ordenes', methods=['GET'])
def get_ordenes():
    return jsonify(ordenes)

# Crear una nueva orden
@app.route('/ordenes', methods=['POST'])
def crear_orden():
    nueva_orden = request.json
    ordenes.append(nueva_orden)
    return jsonify(nueva_orden), 201