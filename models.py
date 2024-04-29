from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Consumidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ordenes = db.relationship('Orden', backref='consumidor', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }
    
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    ordenes = db.relationship('Orden', backref='producto', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock
        }
    
class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumidor_id = db.Column(db.Integer, db.ForeignKey('consumidor.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer)

    consumidor_id = db.Column(db.Integer, db.ForeignKey('consumidor.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'consumidor_id': self.consumidor_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad
        }

# Importa las clases de modelo al final del archivo
from models import Consumidor, Producto, Orden