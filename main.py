from flask import Flask, render_template, request, flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos

import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/index", methods = ["GET", "POST"])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == "POST":
        alum = Alumnos(nombre = create_form.nombre.data,
                       apaterno = create_form.apaterno.data,
                       email = create_form.email.data)
        
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form = create_form)


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    nom = None
    apa = None
    ama = None
    edad = None
    email = None

    if request.method == "POST" and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data

        print("Nombre: ".format(nom))
        print("Apellido Paterno: ".format(apa))
        print("Apellido Materno: ".format(ama))
        print("Email: ".format(email))
        print("Edad: ".format(edad))

        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)

    return render_template(
        "alumnos.html",
        form=alumno_clase,
        nom=nom,
        apa=apa,
        ama=ama,
        email=email,
        edad=edad,
    )


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run()
