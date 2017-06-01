# -*- coding: utf-8 -*-
"""
@author: Pau Vilanova Marco
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
class Telemetria(db.Model):
    __tablename__ = 'Telemetria'
    
    id      = db.Column(db.Integer, primary_key=True)
    shutdown   = db.Column(db.String(200))
    time  = db.Column(db.DateTime)
    Temps_volta = db.Column(db.Integer)
    Sensors_pedals_apps1= db.Column(db.Integer)
    Sensors_pedals_apps2= db.Column(db.Integer)
    Sensors_pedals_brake= db.Column(db.Integer)
    Sensors_direccio= db.Column(db.Integer)
    Sensors_suspensió_front_left= db.Column(db.Integer)
    Sensors_suspensió_front_right= db.Column(db.Integer)
    Sensors_suspensió_rear_left= db.Column(db.Integer)
    Sensors_suspensió_rear_right= db.Column(db.Integer)
    Sensors_velocitat_dreta= db.Column(db.Integer)
    Sensors_velocitat_esquerra=db.Column(db.Integer)
    Bateria_temp_lmin= db.Column(db.Integer)
    Bateria_temp_lmax= db.Column(db.Integer)
    Bateria_temp_min= db.Column(db.Integer)
    Bateria_temp_max= db.Column(db.Integer)
    Bateria_voltage_total= db.Column(db.Integer)
    Bateria_voltage_min= db.Column(db.Integer)
    Bateria_voltage_max= db.Column(db.Integer)

    
	# La otra parte para conectar con Usuarios
    #autor = db.relationship("Usuarios", back_populates="mensajes")
    
    def __init__(self, shutdown, Temps_volta, Sensors_pedals_apps1, Sensors_pedals_apps2, Sensors_pedals_brake, Sensors_direccio, Sensors_suspensió_front_left, Sensors_suspensió_front_right, Sensors_suspensió_rear_left, Sensors_suspensió_rear_right, Bateria_temp_lmin, Bateria_temp_lmax, Bateria_temp_min, Bateria_temp_max, Bateria_voltage_total, Bateria_voltage_min, Bateria_voltage_max,Sensors_velocitat_dreta,Sensors_velocitat_esquerra):
        self.shutdown   = shutdown
        self.time  = datetime.datetime.now()
        self.Temps_volta = Temps_volta
        self.Sensors_pedals_apps1 =Sensors_pedals_apps1
        self.Sensors_pedals_apps2 = Sensors_pedals_apps2
        self.Sensors_pedals_brake = Sensors_pedals_brake
        self.Sensors_direccio = Sensors_direccio
        self.Sensors_suspensió_front_left = Sensors_suspensió_front_left
        self.Sensors_suspensió_front_right = Sensors_suspensió_front_right
        self.Sensors_suspensió_rear_left = Sensors_suspensió_rear_left
        self.Sensors_suspensió_rear_right = Sensors_suspensió_rear_right
        self.Bateria_temp_lmin = Bateria_temp_lmin
        self.Bateria_temp_lmax = Bateria_temp_lmax
        self.Bateria_temp_max = Bateria_temp_max
        self.Bateria_temp_min = Bateria_temp_min
        self.Bateria_voltage_max = Bateria_voltage_max
        self.Bateria_voltage_min = Bateria_voltage_min
        self.Bateria_voltage_total = Bateria_voltage_total
        self.Sensors_velocitat_dreta = Sensors_velocitat_dreta
        self.Sensors_velocitat_esquerra = Sensors_velocitat_esquerra



		
    def __repr__(self):
        # Debe devolver string
        return 'shutdown %r, hora %r, Temps_volta %r, Sensors_pedals_apps1 %r,Sensors_pedals_apps2 %r, Sensors_pedals_brake %r, Sensors_direccio %r, Sensors_suspensió_front_left %r, Sensors_suspensió_front_right %r, Sensors_suspensió_rear_left %r, Sensors_suspensió_rear_right %r, Bateria_temp_lmax %r, Bateria_temp_lmin %r, Bateria_temp_max %r, Bateria_temp_min %r, Bateria_voltage_max %r, Bateria_voltage_min %r, Bateria_voltage_total %r' % (self.shutdown, self.hora, self.Temps_volta, self.Sensors_pedals_apps1, self.Sensors_pedals_apps2, self.Sensors_pedals_brake, self.Sensors_direccio, self.Sensors_suspensió_front_left, self.Sensors_suspensió_front_right, self.Sensors_suspensió_rear_left, self.Sensors_suspensió_rear_right, self.Bateria_temp_lmin, self.Bateria_temp_lmax, self.Bateria_temp_max, self.Bateria_temp_min, self.Bateria_voltage_max, self.Bateria_voltage_min, self.Bateria_voltage_total)

