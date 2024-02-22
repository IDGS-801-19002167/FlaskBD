# WTF imports
from wtforms import Form
from wtforms import validators
from wtforms import StringField,TelField, IntegerField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email

# Flask imports
from flask_wtf import FlaskForm

# Class
class UserForm(Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingresa nombre valido")
    ])
    
    edad = IntegerField("edad", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    
    email = EmailField("email", [
        validators.Email(message="Ingresa un correo valido"),
        validators.length(min=4, max=10, message="Ingresa un correo valido")
    ]) 
    
    apaterno = StringField("apaterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingresa un Apellido valido")
    ])
    
    amaterno = StringField("amaterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingresa un Apellido valido")
    ])
    