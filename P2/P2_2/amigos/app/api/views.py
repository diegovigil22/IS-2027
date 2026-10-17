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