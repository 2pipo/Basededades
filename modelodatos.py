# -*- coding: utf-8 -*-
"""
@author: Samir Kanaan
"""
from inicia import db

# Aquí se definen las tablas de la APP, con las columnas que tendrán, su
# tipo y las formas de crear (__init__) y visualizar (__repr__) un elemento
# de ese tipo.

# Tabla de usuarios
# En realidad habría que encriptar la contraseña (paquete passlib)
class Usuarios(db.Model):
    __tablename__ = "usuarios"
    
    id       = db.Column(db.Integer, primary_key=True)
    nombre   = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(40))
    
    def __init__(self, nombre, password):
        self.nombre   = nombre
        self.password = password
        
    def __repr__(self):
        # Debe devolver string
        return 'Id %r nombre %r' % (self.id, self.nombre)
        
        

# Tabla de mensajes (clave externa idAutor)
import datetime
class Mensajes(db.Model):
    __tablename__ = 'mensajes'
    
    id      = db.Column(db.Integer, primary_key=True)
    texto   = db.Column(db.String(200))
    tiempo  = db.Column(db.DateTime)
    idAutor = db.Column(db.Integer, None, db.ForeignKey('usuarios.id'))
    
    def __init__(self, texto, idAutor):
        self.texto   = texto
        self.tiempo  = datetime.datetime.now()
        self.idAutor = idAutor
        
    def __repr__(self):
        # Debe devolver string
        return 'Texto %r, idAutor %r' % (self.texto, self.idAutor)

