import sys
import os

# Ruta del directorio principal de la aplicación
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importa la aplicación Flask
from app import app as application

# Establece la variable de entorno (si es necesario)
os.environ['FLASK_ENV'] = 'production'
