from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
from schemas.general import IdListSchema
from schemas.student import StudentSchema

students_views = Blueprint('students_views', __name__)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students',
                      methods=['GET', 'POST', 'DELETE'])
def students(departament_id, group_id):
    student_schema = StudentSchema(many=True)

    if request.method == 'GET':
        query_res = query_db('SELECT s.* FROM students AS s '
                             'JOIN groups AS g ON s.group_id = g.id '
                             'JOIN departaments AS d ON g.departament_id = d.id '
                             'WHERE d.id=? AND g.id=?', (departament_id, group_id))
        res = student_schema.load(query_res)
        return jsonify(res.data)
    elif request.method == 'POST':
        # TODO валидация
        student_schema = StudentSchema(many=True).loads(request.data)
        if not student_schema.errors:
            student_data = student_schema.data
            res = 'Ok'
            for s in student_data:
                query_db("INSERT INTO students (name, gender, birth_date, phone_number, group_id) "
                         "VALUES (?,?,?,?,?)", (s['name'], s['gender'],
                                                s.get('birth_date'), s.get('phone_number'),
                                                group_id))
            get_db().commit()
        else:
            res = student_schema.errors
        return jsonify(res)
    elif request.method == 'DELETE':
        # TODO добавить детальную обработку запроса (вывод информации о удалении, либо об отсутствии студентов
        # TODO с таким id)
        id_schema = IdListSchema().loads(request.data)
        if not id_schema.errors:
            question_marks = ['?'] * (len(id_schema.data) + 1)
            res = query_db("delete from students where id in ({question_marks});"
                           .format(question_marks=','.join(question_marks)), id_schema.data['id_list'])
            get_db().commit()
        else:
            res = id_schema.errors
        return jsonify(res)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students/<int:student_id>',
                      methods=['GET', 'PUT', 'DELETE'])
def student(departament_id, group_id, student_id):
    if request.method == 'GET':
        res = query_db('SELECT s.* FROM students AS s '
                       'JOIN groups AS g ON s.group_id = g.id '
                       'JOIN departaments AS d ON g.departament_id = d.id '
                       'WHERE d.id=? AND g.id=? AND s.id=?', (departament_id, group_id, student_id))
        return jsonify(res)
    elif request.method == 'PUT':
        student_schema = StudentSchema(field_requirement=False).loads(request.data)
        res = 'Ok'
        if not student_schema.errors:
            for field in student_schema.data:
                query_db('update students set {field_name}=? where id=?'.format(field_name=field),
                         (student_schema.data[field], student_id))
            get_db().commit()
        else:
            res = student_schema.errors
        return jsonify(res)
    elif request.method == 'DELETE':
        res = query_db("DELETE FROM students WHERE id=?;", (student_id,))
        get_db().commit()
        return jsonify('Ok')
