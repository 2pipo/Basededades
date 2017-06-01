#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Pau Vilanova Marco
"""

from inicia_1 import db

# Importar las tablas del modelo de datos que hayamos definido
from modelodatos_1 import *


# Generar las tablas en la BD
if __name__ == '__main__':
    db.create_all()
    
    # Aquí se podría añadir código para cargar datos iniciales en la BD.

