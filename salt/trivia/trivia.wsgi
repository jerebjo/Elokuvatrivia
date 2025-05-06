import sys
import logging
from os import environ

# Lisää sovelluksen polku
sys.path.insert(0, '/var/www/trivia')

# Flask-sovelluksen tuominen
from app import app as application

# Asetetaan logitus
logging.basicConfig(stream=sys.stderr)
application.debug = True
