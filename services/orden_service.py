from flask import jsonify
from models import Orden, db

def obtener_ordenes():
    ordenes = Orden.query.all()
    return jsonify([orden.serialize() for orden in ordenes])

def crear_orden(orden_nuevo):
    temporal = Orden(consumidor_id = orden_nuevo['consumidor_id'], producto_id = orden_nuevo['producto_id'], cantidad = orden_nuevo['cantidad'])
    db.session.add(temporal)
    db.session.commit()
    return jsonify(temporal.serialize()), 201