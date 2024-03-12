from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Alumnos(db.Model):
    __tablename__ = "alumnos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

class Pizza(db.Model):
    __tablename__ = "orden"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    cantidad = db.Column(db.Integer)
    tamanio = db.Column(db.String(100))
    precio = db.Column(db.Float())
    ingredientes = db.Column(db.String(100), nullable = False)
    dia = db.Column(db.String(10))
    mes = db.Column(db.String(10))
    anio = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Ventas(db.Model):
    __tablename__ = "venta"
    id = db.Column(db.Integer, primary_key=True)
    nombreC = db.Column(db.String(100))
    pagoTotal = db.Column(db.Float())
    dia = db.Column(db.String(10))
    mes = db.Column(db.String(10))
    anio = db.Column(db.Integer)
    created_at  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
