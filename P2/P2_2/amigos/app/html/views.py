from flask import render_template, redirect, url_for, request, abort
from .. import db
from . import html
from ..models import Amigo


@html.route("/amigos")
def tabla_amigos():
    """
    Obtiene la lista de amigos de la base de datos y la
    devuelve en una tabla HTML.
    """
    amigos = Amigo.query.all()
    return render_template("tabla_amigos.html",
                           amigos=amigos)

@html.route("/delete_amigo/<int:id>")
def delete_amigo(id):
    """
    Borra un amigo de la base de datos.
    """
    amigo = Amigo.query.get_or_404(id)

    db.session.delete(amigo)
    db.session.commit()

    return redirect(url_for('html.tabla_amigos'))

@html.route("/edit_amigo/<int:id>")
def edit_amigo(id):
    """
    Presenta un formulario para obtener datos a modificar de un amigo.
    """
    amigo = Amigo.query.get_or_404(id)

    return render_template("edit_amigo.html", amigo=amigo)

@html.route("/new_amigo/")
def new_amigo():
    """
    Presenta un formulario para obtener datos para crear un nuevo amigo.
    """
    return render_template("edit_amigo.html", amigo=None)

@html.route("/save_amigo", methods=["POST"])
def save_amigo():
    id = request.form.get("id")

    if id is None or id == "":
        # En este caso se trata de un amigo nuevo, lo creamos.
        name = request.form.get("name")

        if not name:
            # Si falta el nombre, devolvemos un error HTTP 422
            abort(422)

        # Valores por defecto si los campos no vienen en el formulario.
        lati = request.form.get("lati", "0")
        longi = request.form.get("longi", "0")
        # Creamos el amigo y lo añadimos a la base de datos
        amigo = Amigo(name=name, lati=lati, longi=longi)
        db.session.add(amigo)
        db.session.commit()
    else:
        # En este caso se trata de un amigo de la base de datos.
        amigo = Amigo.query.get_or_404(int(id))
        # Modificamos los campos que vengan en el formulario
        name = request.form.get("name")
        if name:
            amigo.name = name

        lati = request.form.get("lati")
        if lati:
            amigo.lati = lati

        longi = request.form.get("longi", "0")
        if longi:
            amigo.longi = longi
        # Una vez modificado, lo guardamos a la base de datos
        db.session.commit()
    # Redireccionamos hacia la tabla-lista de amigos
    return redirect(url_for("html.tabla_amigos"))