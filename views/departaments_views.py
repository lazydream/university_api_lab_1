from flask import Blueprint, jsonify

from db_utils import query_db
from utils import format_departaments

departaments_views = Blueprint('departaments_views', __name__)

@departaments_views.route('/departaments')
def departaments():
    departaments = query_db('select * from departaments')
    res = format_departaments(departaments)
    return jsonify(res)


@departaments_views.route('/departaments/<int:departament_id>')
def departament(departament_id):
    departament = query_db('select * from departaments '
                           'where id={departament_id}'
                           .format(departament_id=departament_id))
    res = format_departaments(departament)
    return jsonify(res)
