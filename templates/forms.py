
from wtforms import Form
from wtforms import validators
from wtforms import StringField,TelField, IntegerField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email


from flask_wtf import FlaskForm


class UserForm(Form):
    id = IntegerField("id", [validators.number_range(min=1, max=20, message = "valor no valido")])
    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingresa nombre valido")
    ])
    
    email = EmailField("correo", [
        validators.DataRequired(message="Ingresa un correo valido"),
        validators.Email(message="Ingresa un correo valido")
    ]) 
    
    apaterno = StringField("apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    