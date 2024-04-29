from flask import jsonify
from models import Orden, Consumidor, Producto, db

def obtener_ordenes():
    ordenes = Orden.query.all()
    return jsonify([orden.serialize() for orden in ordenes])

# def crear_orden(orden_nuevo):
#     temporal = Orden(consumidor_id = orden_nuevo['consumidor_id'], producto_id = orden_nuevo['producto_id'], cantidad = orden_nuevo['cantidad'])
#     db.session.add(temporal)
#     db.session.commit()
#     return jsonify(temporal.serialize()), 201

def crear_orden(orden_nuevo):
    consumidor = Consumidor.query.get(orden_nuevo['consumidor_id'])
    if not consumidor:
        return jsonify({'error': 'Consumidor no encontrado'}), 404

    producto = Producto.query.get(orden_nuevo['producto_id'])
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    nueva_orden = Orden(consumidor_id=orden_nuevo['consumidor_id'], 
                        producto_id=orden_nuevo['producto_id'], 
                        cantidad=orden_nuevo['cantidad'])
    db.session.add(nueva_orden)
    db.session.commit()

    return jsonify(nueva_orden.serialize()), 201

def actualizar_orden(id, new_data):
    orden = Orden.query.get(id)

    if orden is None:
        return jsonify({'error': 'Orden no encontrada'}), 404

    orden.consumidor_id = new_data['consumidor_id']
    orden.producto_id = new_data['producto_id']
    orden.cantidad = new_data['cantidad']
    db.session.commit()
    return jsonify(orden.serialize())

def eliminar_orden(id):
    orden = Orden.query.get(id)
    if orden is None:
        return jsonify({'error': 'Orden no encontrada'}), 404
    db.session.delete(orden)
    db.session.commit()
    return jsonify({'message': 'Orden eliminada correctamente'})