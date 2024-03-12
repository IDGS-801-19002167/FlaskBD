# WTF imports
from wtforms import Form
from wtforms import validators
from wtforms import StringField,TelField, IntegerField, RadioField, FloatField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email

# Flask imports
from flask_wtf import FlaskForm

class Pizza(Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message="Nombre requerido")
    ])

    direccion = StringField("direccion", [
        validators.DataRequired(message="Direccion requerida")
    ])

    telefono = StringField("telefono", [
        validators.DataRequired(message="Telefono requerido")
    ])

    cantidad = IntegerField("cantidad", [
        validators.DataRequired(message="Cantidad requerida")
    ])

    tamanio = RadioField("rdo", [
        validators.DataRequired(message="Tamaño requerido")
    ])

    precio = FloatField("precio")

    ingredientes = StringField("ingredientes")

    dia = StringField("dia", [
        validators.DataRequired(message="Dia de venta requerido"),
        validators.length(min=5, max=10)
    ])

    mes = StringField("mes", [
        validators.DataRequired(message="Mes de venta requerido"),
        validators.length(min=5, max=10)
    ])

    anio = IntegerField("anio", [
        validators.DataRequired(message="Año de venta requerido"),
        validators.NumberRange(min=4, max=4)
    ])

class Ventas(Form):
    nombre = StringField("nombre")

    totalVenta = FloatField("totalVenta")

class PizzaE(Form):
    id = IntegerField('id')

    nombre = StringField("nombre", [
        validators.DataRequired(message="Nombre requerido")
    ])

    direccion = StringField("direccion", [
        validators.DataRequired(message="Direccion requerida")
    ])

    telefono = StringField("telefono", [
        validators.DataRequired(message="Telefono requerido")
    ])

    cantidad = IntegerField("cantidad", [
        validators.DataRequired(message="Cantidad requerida")
    ])

    tamanio = RadioField("rdo", [
        validators.DataRequired(message="Tamaño requerido")
    ])

    precio = FloatField("precio")

    ingredientes = StringField("ingredientes")

    dia = StringField("dia", [
        validators.DataRequired(message="Dia de venta requerido"),
        validators.length(min=5, max=10)
    ])

    mes = StringField("mes", [
        validators.DataRequired(message="Mes de venta requerido"),
        validators.length(min=5, max=10)
    ])

    anio = IntegerField("anio", [
        validators.DataRequired(message="Año de venta requerido"),
        validators.NumberRange(min=4, max=4)
    ])