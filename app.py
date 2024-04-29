from flask import Flask, request
from models import Consumidor, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from services.consumidores_service import obtener_consumidores, crear_consumidor, actualizar_consumidor, eliminar_consumidor
from services.productos_service import obtener_productos, crear_producto
from services.orden_service import obtener_ordenes, crear_orden


############################################## Rutas de consumidores

@app.route('/consumidores', methods=['GET'])
def get_consumidores():
    return obtener_consumidores()

@app.route('/consumidores', methods=['POST'])
def create_cunsumidor():
    return crear_consumidor(request.json)

@app.route('/consumidores', methods=['PUT'])
def update_consumidor():
    return actualizar_consumidor(request.json)


@app.route('/consumidores/<int:id>', methods=['DELETE'])
def delete_consumidor(id):
    return eliminar_consumidor(id)


############################################## Rutas de productos

@app.route('/producto', methods=['GET'])
def get_productos():
    return obtener_productos()

@app.route('/producto', methods=['POST'])
def create_producto():
    return crear_producto(request.json)

# @app.route('/producto', methods=['PUT'])
# def update_():
#     return actualizar_consumidor(request.json)


# @app.route('/producto/<int:id>', methods=['DELETE'])
# def delete_consumidor(id):
#     return eliminar_consumidor(id)


############################################## Rutas de ordenes

@app.route('/orden', methods=['GET'])
def get_ordenes():
    return obtener_ordenes()

@app.route('/orden', methods=['POST'])
def create_orden():
    return crear_orden(request.json)
    


if __name__ == '__main__':
    app.run(debug=True)