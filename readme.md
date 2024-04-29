# Proyecto de Registro de Consumidores y Órdenes

Este proyecto implementa un sistema para registrar consumidores con su información básica, una serie de productos con descripción, precio y cantidad en stock, y órdenes que reflejan las compras de los consumidores.

## Configuraciones Iniciales

### Instalación de Paquetes

Para ejecutar la aplicación, asegúrate de tener Python instalado en tu sistema. Luego, instala los paquetes necesarios ejecutando el siguiente comando en tu terminal:

```bash
pip install Flask
```

```bash
pip install flask_sqlalchemy
```

Esto instalará todas las dependencias necesarias para ejecutar la aplicación, incluyendo Flask y SQLAlchemy.

### Inicialización de la Base de Datos
Antes de ejecutar la aplicación, necesitas inicializar la base de datos. Para hacerlo, ejecuta el siguiente comando en tu terminal:

```bash
python init_db.py
```

## Ejecución de la Aplicación
Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

```bash
python app.py
```

Esto iniciará el servidor de desarrollo y podrás acceder a la aplicación desde tu navegador en la dirección http://localhost:5000.

En el archivo **Prueba Natalia.postman_collection.json** encontrará más información sobre los endpoints

