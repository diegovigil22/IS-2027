from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo

@api.route("/amigo/<int:id>")
def get_amigo(id):
    """
    Retorna JSON con información sobre el amigo cuyo id recibe
    o un error 404 si no lo encuentra.
    """
    amigo = Amigo.query.get_or_404(id)
    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi
    }

    return jsonify(amigodict)

@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    """
    Busca un amigo por su nombre y retorna sus datos en JSON.
    Si no existe, retorna un error 404.
    """
    amigo = Amigo.query.filter_by(name=name).first()

    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")

    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi
    }

    return jsonify(amigodict)

@api.route("/amigos")
def list_amigos():
    """
    Retorna un JSON con la lista de amigos.
    """
    amigos = Amigo.query.all()
    lista = []

    for amigo in amigos:
        amigodict = {
            'id': amigo.id,
            'name': amigo.name,
            'lati': amigo.lati,
            'longi': amigo.longi
        }

        lista.append(amigodict)

    return jsonify(lista)

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    """
    Modifica un amigo y retorna sus datos actualizados en JSON.
    """
    # Obtenemos el amigo a partir de su ID
    amigo = Amigo.query.get_or_404(id)

    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Intentamos extraer campos del JSON
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")

    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi

    # Finalmente, si hemos cambiado algo en el objeto amigo, hacemos
    # el commit a la base de datos para que se guarden las modificaciones
    if name or lati or longi:
        db.session.commit()

    # Y retornamos el JSON con los nuevos datos
    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "longi": amigo.longi,
        "lati": amigo.lati
    }

    return jsonify(amigodict)

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    """
    Elimina de la base de datos el amigo indicado.
    """
    amigo = Amigo.query.get_or_404(id)

    db.session.delete(amigo)
    db.session.commit()

    return ('', 204)

@api.route("/amigos", methods=["POST"])
def new_amigo():
    """
    Crea un amigo con los datos recibidos en JSON
    y retorna sus datos, incluido el identificador.
    """
    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Intentamos extraer campos del JSON
    name = request.json.get("name")
    # Si no hay nombre, rechazamos la petición
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")

    # Si el nombre ya existe en la base de datos, también lo rechazamos
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")

    # En caso contrario, tomamos latitud y longitud. Si no vienen les
    # damos un valor de 0
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")

    # Creamos un nuevo amigo con esos datos
    amigo = Amigo(name=name, lati=lati, longi=longi)
    db.session.add(amigo)
    db.session.commit()

    # Y retornamos el JSON con los datos del nuevo amigo
    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "longi": amigo.longi,
        "lati": amigo.lati
    }

    return jsonify(amigodict)