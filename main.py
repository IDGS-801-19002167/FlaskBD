from flask import Flask, render_template, request, flash, g, redirect, url_for, jsonify
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos, Pizza, Ventas
from forms import UserForm, UserForm2
import forms, forms2

# from localStorage import localStoragePy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)

# arrayOrders = []


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# id,nombre,direccion,telefono,correo,sueldo


@app.route("/index", methods=["GET", "POST"])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data,
        )

        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=create_form)


@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()

    return render_template("ABC_Completo.html", alumno=alum_form, alumnos=alumno)


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


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = UserForm2(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email

    if request.method == "POST":
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect("/ABC_Completo")

    return render_template("eliminar.html", form=create_form)


@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = UserForm2(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
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
        return redirect("/ABC_Completo")

    return render_template("modificar.html", form=create_form)

@app.route("/pizza", methods=["GET", "POST"])
def pizzas():
    # form_p = forms2.Pizza(request.form)
    # form_d = forms2.PizzaE(request.form)
    # ingredientes = []
    # ventas = Ventas.query.all()

    # if request.method == "POST":
    #     precio = form_p.precio.data
    #     tamanio = form_p.tamanio.data
    #     cantidad = form_p.cantidad.data
    #     jamon = request.form.get('jamon')
    #     pinia = request.form.get('pinia')
    #     champ = request.form.get('champ')

    #     if jamon is not None:
    #         ingredientes.append('Jamón')
    #     if pinia is not None:
    #         ingredientes.append('Piña')
    #     if champ is not None:
    #         ingredientes.append('Champiñones')

    #     size = 0

    #     if len(ingredientes) == 1:
    #         size = 10
    #     elif len(ingredientes) == 2:
    #         size = 20
    #     elif len(ingredientes) == 3:
    #         size = 30
    #     else:
    #         size = 0

    #     if tamanio == 'chica':
    #         precio = (40 * int(cantidad)) + size
    #     elif tamanio == 'mediana':
    #         precio = (80 * int(cantidad)) + size
    #     elif tamanio == 'grande':
    #         precio = (120 * int(cantidad)) + size

    #     pizzaDB = Pizza(
    #         nombre=form_p.nombre.data,
    #         direccion=form_p.direccion.data,
    #         telefono=form_p.telefono.data,
    #         cantidad=form_p.cantidad.data,
    #         tamanio=form_p.tamanio.data,
    #         precio=precio,
    #         ingredientes=size,
    #         dia=request.form.get('filterday'),
    #         mes=request.form.get('filtermonth'),
    #         anio=form_p.anio.data
    #     )

    #     # db.session.add(pizzaDB)
    #     # db.session.commit()
    #     # return jsonify({'message': "Pizza agregada con exito"})

    # return redirect("/pizzeria")
    datos_json = request.get_json()
    
    if request.method == "POST":
        precio = 0
        tamanio = datos_json['tamanio']
        cantidad = datos_json['cantidad']
        jamon = datos_json['ingredientes']['jamon']
        pinia = datos_json['ingredientes']['pinia']
        champ = datos_json['ingredientes']['champ']

        ingredientes = []

        if jamon is not False:
            ingredientes.append('Jamón')
        if pinia is not False:
            ingredientes.append('Piña')
        if champ is not False:
            ingredientes.append('Champiñones')

        size = 0

        if len(ingredientes) == 1:
            size = 10
        elif len(ingredientes) == 2:
            size = 20
        elif len(ingredientes) == 3:
            size = 30
        else:
            size = 0

        if tamanio == 'chica':
            precio = (40 * int(cantidad)) + size
        elif tamanio == 'mediana':
            precio = (80 * int(cantidad)) + size
        elif tamanio == 'grande':
            precio = (120 * int(cantidad)) + size

        pizzaDB = Pizza(
            nombre=datos_json['nombre'],
            direccion=datos_json['direccion'],
            telefono=datos_json['telefono'],
            cantidad=datos_json['cantidad'],
            tamanio=datos_json['tamanio'],
            precio=precio,
            ingredientes=size,
            dia=datos_json['dia'],
            mes=datos_json['mes'],
            anio=datos_json['anio']
        )

        db.session.add(pizzaDB)
        db.session.commit()
        return jsonify({'message': "Pizza agregada con exito"})


@app.route("/pizzeria", methods=["GET"])
def pizzeria():
    form_p = forms2.Pizza(request.form)
    ventas = Ventas.query.all()

    return render_template("pizza.html", form=form_p, ventas=ventas)


@app.route("/orders", methods=["GET"])
def getorders():
    orden = Pizza.query.all()
    all_orders = [{'tamanio': o.tamanio, 'ingredientes': o.ingredientes, 'cantidad': o.cantidad, 'precio': o.precio,
                   'id': o.id, 'nombre': o.nombre, 'dia': o.dia, 'mes': o.mes, 'anio': o.anio} for o in orden]

    return jsonify(all_orders)


@app.route("/itemedit", methods=["GET", "POST"])
def edit():
    form_e = forms2.PizzaE(request.form)
    ingredientes = []
    dia_seleccionado = None
    mes_seleccionado = None

    if request.method == "GET":
        id = request.args.get('id')
        item = db.session.query(Pizza).filter(Pizza.id == id).first()
        form_e.id.data = request.args.get('id')
        form_e.nombre.data = item.nombre
        form_e.direccion.data = item.direccion
        form_e.telefono.data = item.telefono
        form_e.cantidad.data = item.cantidad
        form_e.precio.data = item.precio
        dia_seleccionado = item.dia
        mes_seleccionado = item.mes
        form_e.anio.data = item.anio

    if request.method == "POST":
        id = form_e.id.data
        item = db.session.query(Pizza).filter(Pizza.id == id).first()
        item.precio = 0

        precio = form_e.precio.data
        tamanio = form_e.tamanio.data
        cantidad = form_e.cantidad.data
        jamon = request.form.get('jamon')
        pinia = request.form.get('pinia')
        champ = request.form.get('champ')

        if jamon is not None:
            ingredientes.append('Jamón')
        if pinia is not None:
            ingredientes.append('Piña')
        if champ is not None:
            ingredientes.append('Champiñones')

        size = 0

        if len(ingredientes) == 1:
            size = 10
        elif len(ingredientes) == 2:
            size = 20
        elif len(ingredientes) == 3:
            size = 30
        else:
            size = 0

        if tamanio == 'chica':
            precio = (40 * int(cantidad)) + size
        elif tamanio == 'mediana':
            precio = (80 * int(cantidad)) + size
        elif tamanio == 'grande':
            precio = (120 * int(cantidad)) + size

        item.nombre = form_e.id.data
        item.direccion = form_e.direccion.data
        item.telefono = form_e.telefono.data
        item.cantidad = form_e.cantidad.data
        item.precio = precio
        item.dia = form_e.dia.data
        item.mes = form_e.mes.data
        item.anio = form_e.anio.data
        item.ingredientes = size
        db.session.commit()

        return redirect('/pizza')

    return render_template('modificarPizza.html', form=form_e, dia=dia_seleccionado, mes=mes_seleccionado)


@app.route("/deleteitem", methods=["GET", "POST"])
def delitem():
    item_d = request.get_json()

    if request.method == "POST":
        id = item_d['id']
        item = Pizza.query.get(id)

        if item:
            db.session.delete(item)
            db.session.commit()

    return redirect("/pizzeria")


@app.route('/filtrar', methods=["GET", "POST"])
def filtrar():
    datos = request.get_json()
    resultados = []
    
    try:
        if request.method == "POST":
            filterday = datos['filterday']
            filtermonth = datos['filtermonth']
            filteranio = datos['filteranio']
            filtercustomer = datos['filtercustomer']

            if filterday is not None and filtermonth is None and filteranio == "":
                resultados = db.session.query(Ventas).filter(Ventas.dia == filterday).all()
            elif filtermonth is not None and filterday is None and filteranio == "":
                resultados = db.session.query(Ventas).filter(Ventas.mes == filtermonth).all()
            elif filteranio != "" and filterday is None and filtermonth is None:
                resultados = db.session.query(Ventas).filter(Ventas.anio == filteranio).all()
            elif filtercustomer != "" and filterday is None and filtermonth is None and filteranio == "":
                resultados = db.session.query(Ventas).filter(Ventas.nombreC == filtercustomer).all()

        resultados_json = [{'nombreC': r.nombreC,
                            'pagoTotal': r.pagoTotal} for r in resultados]

    except Exception as ex:
        return jsonify({"error": "Solo 1"})

    return jsonify({'resultados': resultados_json})


@app.route('/venta', methods=['POST'])
def venta():
    data = request.get_json()

    try:
        for item in data:
            venta = Ventas(
                nombreC=item.get('nombre'),
                pagoTotal=item.get('subtotal'),
                dia=item.get('dia'),
                mes=item.get('mes'),
                anio=item.get('anio')
            )

            db.session.add(venta)

            id = item.get('id')

            p = Pizza.query.get(id)

            if p:
                db.session.delete(p)

        db.session.commit()

        return jsonify({'message': "Venta realizada con éxito"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Ocurrió un error"})

    return redirect('/pizza')


def realizar_filtrado(filtro, valor):
    return {'resultados': ['Resultado 1', 'Resultado 2']}



if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run()
