from flask import jsonify
from models import Consumidor, db

def obtener_consumidores():
    consumidores = Consumidor.query.all()
    return jsonify([consumidor.serialize() for consumidor in consumidores])

def crear_consumidor(nuevo_consumidor):
    nuevo_consumidor = Consumidor(nombre=nuevo_consumidor['nombre'])
    db.session.add(nuevo_consumidor)
    db.session.commit()
    return jsonify(nuevo_consumidor.serialize()), 201

def actualizar_consumidor(new_data):
    consumidor = Consumidor.query.get(new_data["id"])

    if consumidor is None:
        return jsonify({'error': 'Consumidor no encontrado'}), 404

    consumidor.nombre = new_data['nombre']
    db.session.commit()
    return jsonify(consumidor.serialize())

def eliminar_consumidor(id):
    consumidor = Consumidor.query.get(id)
    if consumidor is None:
        return jsonify({'error': 'Consumidor no encontrado'}), 404
    db.session.delete(consumidor)
    db.session.commit()
    return jsonify({'message': 'Consumidor eliminado correctamente'})