from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
from schemas.departaments import DepartamentsSchema
from schemas.general import IdListSchema
from utils import format_departaments

departaments_views = Blueprint('departaments_views', __name__)


@departaments_views.route('/departaments',
                          methods=['GET', 'POST', 'DELETE'])
def departaments():
    departaments_sch = DepartamentsSchema(many=True)
    res = {}
    if request.method == 'GET':
        departaments_data = query_db('SELECT * FROM departaments')

        departaments_groups = query_db('SELECT d.id FROM departaments AS d '
                                       'WHERE exists (SELECT * FROM groups AS g '
                                       'WHERE g.departament_id=d.id)')

        departaments_teachers = query_db('SELECT d.id FROM departaments AS d '
                                         'WHERE exists(SELECT * FROM teachers AS t '
                                         'WHERE d.id=t.departament_id)')

        res = format_departaments(departaments_sch.load(departaments_data).data,
                                  departaments_groups,
                                  departaments_teachers)
    elif request.method == 'POST':
        new_departaments = departaments_sch.loads(request.data)
        if not new_departaments.errors:
            for d in new_departaments.data:
                query_db('INSERT INTO departaments (name, institute) '
                         'VALUES (?,?) ', (d.get('name'), d.get('institute')))
            get_db().commit()
            res = 'Ok'
        else:
            res = new_departaments.errors
    elif request.method == 'DELETE':
        id_list = IdListSchema().loads(request.data)
        if not id_list.errors:
            question_marks = ['?'] * len(id_list.data['id_list'])
            query_db('delete from departaments '
                     'where id in ({question_marks})'
                     .format(question_marks=','.join(question_marks)),
                     id_list.data['id_list'])
            get_db().commit()
            res = 'Ok'
        else:
            res = id_list.errors
    return jsonify(res)


@departaments_views.route('/departaments/<int:departament_id>',
                          methods=['GET', 'PUT', 'DELETE'])
def departament(departament_id):
    res = {}
    status_code = 200
    if request.method == 'GET':
        departament_data = query_db('SELECT * FROM departaments '
                                    'WHERE id=?', (departament_id,))

        departament_groups = query_db('SELECT d.id FROM departaments AS d '
                                      'WHERE d.id=? AND exists (SELECT * FROM groups AS g '
                                      'WHERE g.departament_id=d.id)', (departament_id,))

        departament_teachers = query_db('SELECT d.id FROM departaments AS d '
                                        'WHERE d.id=? AND exists(SELECT * FROM teachers AS t '
                                        'WHERE d.id=t.departament_id)', (departament_id,))

        res = format_departaments(DepartamentsSchema(many=True).load(departament_data).data,
                                  departament_groups,
                                  departament_teachers)
    elif request.method == 'PUT':
        fields = DepartamentsSchema().loads(request.method)
        if not fields.errors:
            for field in fields.data:
                query_db('update departaments set {field_name}=?'
                         .format(field_name=field),
                         (fields.data[field],))
            get_db().commit()
            res = 'Ok'
        else:
            res = fields.errors
    elif request.method == 'DELETE':
        check = query_db('select count(*) from departaments where id=?', (departament_id,), True)
        if check['count(*)'] > 0:
            query_db('delete from departaments where id=?', (departament_id,))
            get_db().commit()
            res = 'Ok'
        else:
            res = 'Resource has been gone'
            status_code = 410  # Gone
    response = jsonify(res)
    response.status_code = status_code
    return response
