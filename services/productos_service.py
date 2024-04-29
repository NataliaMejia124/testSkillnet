from flask import jsonify
from models import Producto, db

def obtener_productos():
    productos = Producto.query.all()
    return jsonify([producto.serialize() for producto in productos])

def crear_producto(producto_nuevo):
    temporal = Producto(descripcion = producto_nuevo['descripcion'], precio = producto_nuevo['precio'], stock = producto_nuevo['stock'])
    db.session.add(temporal)
    db.session.commit()
    return jsonify(temporal.serialize()), 201

def actualizar_producto(id, new_data):
    producto = Producto.query.get(id)

    if producto is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    producto.descripcion = new_data['descripcion']
    producto.precio = new_data['precio']
    producto.stock = new_data['stock']
    db.session.commit()
    return jsonify(producto.serialize())

def eliminar_producto(id):
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({'error': 'producto no encontrado'}), 404
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'message': 'producto eliminado correctamente'})