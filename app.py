#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:35:19 2016

@author: samir
"""

# RESTful API + postgreSQL DB usando SQLAlchemy

from flask import Flask, request
from flask.ext.restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.httpauth import HTTPBasicAuth

# Crear app y conectar a db
from inicia import app, db

api = Api(app)

# Importar las clases del modelo de datos
from modelodatos import Usuarios, Mensajes


# Para gestionar la autentificación de usuarios
auth = HTTPBasicAuth()

# Esta función debe devolver la contraseña correspondiente al nombre recibido
@auth.get_password
def buscarContrasenya(nombreUsuario):

    usr = Usuarios.query.filter_by(nombre=nombreUsuario).first()
    if usr:
        return usr.password
    else:
        return None



# GESTIÓN DE USUARIOS
class ListaUsuariosAPI(Resource):
    # Los gets requieren identificación del usuario, así que ponemos esto
    @auth.login_required
    def get(self):
        
        #print(request.headers)
        
        # Si llega un GET vacío devolver todos los usuarios; si llega un
        # nombre, devolver solo ese usuario (sirve para verificar q usuario existe).
                
        # Los parámetros que GET recibe después de la URL (?name=xxx&pass?=yyy)
        # están en el diccionario request.args
        if 'nombre' in request.args:
            # El nombre recibido como arg se obtendría así:
            # nombre = request.args.get('nombre')
            # Pero ya hemos leído el usuario del mensaje GET, no hace falta

            return {'nombre': auth.username()}
                
        else:
            usrs = Usuarios.query.all()
            # Devolver aquí atribs o añadir un método a Usuarios. No hace falta
            # devolver todos los datos (password, id)
            return [{'nombre':u.nombre} for u in usrs]
        
    # Cambia el nombre o la contraseña de un usuario, lo que haya en el mensaje
    # El usuario debe identificarse con sus valores anteriores
    @auth.login_required
    def put(self):
        # Obtener el usuario a modificar, cambiar los valores recibidos y
        # grabarlos en la BD
        usuario = Usuarios.query.filter_by(nombre=auth.username()).first()
        

        # Devolverá nombre y/o password, según lo que se haya modificado
        respuesta = {}
        if 'nombre' in request.json:
            usuario.nombre = request.json['nombre']
            respuesta['nombre'] = usuario.nombre
        if 'password' in request.json:
            usuario.password = request.json['password']
            respuesta['password'] = usuario.password

        # Forma más sencilla de actualizar un solo campo:
        # Usuarios.query.filter_by(nombre=nombre).update({Usuarios.nombre:nombre})

        try:
            db.session.commit()
            return respuesta
        except:
            db.session.rollback()
            return {"error": "Error al modificar el usuario"}, 401
            
    
    # Extraer nombre y password de la petición, crear un usuario, añadirlo a la 
    # bd y devolver éxito, o mensaje+código de error si falla y cancelar petición bd
    # No necesita identificación, claro
    def post(self):
        usuario = Usuarios(request.json['nombre'], request.json['password'])
        db.session.add(usuario)
        try:    
            db.session.commit()
            return {'nombre': usuario.nombre}
        except:
            db.session.rollback()
            return {"error": u"Error al añadir el usuario (nombre ya existe?)"}, 401
    
    
    # Borrar el usuario actual (toma nombre de la identificación). 
    @auth.login_required
    def delete(self):
        nombre = auth.username()
        try:
            Usuarios.query.filter_by(nombre=nombre).delete()
            db.session.commit()
            return {'result': True}
        except:
            db.session.rollback()
            return {"error": "Error al borrar el usuario"}, 404
          
 
# GESTIÓN DE LOS MENSAJES
class MensajesAPI(Resource):
    @auth.login_required
    def get(self):
        msjs = Mensajes.query.all()
        
        # Mediante m.autor accedemos a la info del autor gracias a la relationship
        return [{'texto':m.texto, 'tiempo':str(m.tiempo), 'autor':m.autor.nombre} for m in msjs]
    
    # No se pueden modificar los mensajes
    def put(self):
        pass
    
    # Añade un nuevo mensaje
    @auth.login_required
    def post(self):
        # Buscar id del autor para crear el mensaje con ese id
        usuario = Usuarios.query.filter_by(nombre=auth.username()).first()
        
        msj = Mensajes(request.json['texto'], usuario.id)
        db.session.add(msj)
        try:    
            db.session.commit()
            return {'result': True}
        except:
            db.session.rollback()
            return {"error": "Error al añadir el mensaje"}, 404
    
    # Borrar el mensaje con su id (no accesible desde la app)
    @auth.login_required
    def delete(self):
        
        idMsj = request.json['id']
        try:
            Mensajes.query.filter_by(id=id).delete()
            db.session.commit()
            return {'result': True}
        except:
            db.session.rollback()
            return {"error": "Error al borrar el mensaje"}, 404
          

# ACTIVACIÓN DE LOS PUNTOS DE ACCESO API   

api.add_resource(ListaUsuariosAPI, '/msgs/api/v1.0/users', endpoint='users')    
api.add_resource(MensajesAPI, '/msgs/api/v1.0/messages', endpoint='messages')    


if __name__ == '__main__':
    app.run(debug=True)