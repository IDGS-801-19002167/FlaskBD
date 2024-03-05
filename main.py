from flask import Flask, render_template, request, flash, g, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
from forms import UserForm, UserForm2
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# id,nombre,direccion,telefono,correo,sueldo

@app.route("/index", methods = ["GET", "POST"])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == "POST":
        alum = Alumnos(nombre = create_form.nombre.data,
                       apaterno = create_form.apaterno.data,
                       email = create_form.email.data)
        
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form = create_form)

@app.route("/ABC_Completo", methods = ["GET","POST"])
def ABCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", alumno = alum_form, alumnos = alumno)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alumno_clase = UserForm(request.form)
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

@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    create_form = UserForm2(request.form)
    
    if request.method == "GET":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
        
    if request.method == "POST":
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('/ABC_Completo')
        
    return render_template("eliminar.html", form=create_form)


@app.route("/modificar", methods=["GET","POST"])
def modificar():
    create_form = UserForm2(request.form)
    
    if request.method == "GET":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
        
    if request.method == "POST":
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.email = create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect('/ABC_Completo')
        
    return render_template("modificar.html", form=create_form)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run()
