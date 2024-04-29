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