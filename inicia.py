# -*- coding: utf-8 -*-
"""
@author: Samir Kanaan
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

# Configurar la APP y conectar a la base de datos de Heroku o a la local
# si estamos trabajando en local. El resto de ficheros deben importar db y/o 
# app de aquí.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 
    'postgres://postgres:postgres@localhost/MENSAJES')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
db = SQLAlchemy(app)



