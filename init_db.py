from app import app, db

# Inicia el contexto de la aplicación Flask
with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()
