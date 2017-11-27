from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
from schemas.courses import CoursesSchema
from schemas.general import IdListSchema
from schemas.teachers import TeachersSchema
from utils import format_teachers

teachers_views = Blueprint('teachers_views', __name__)


@teachers_views.route('/departaments/<int:departament_id>/teachers',
                      methods=['GET', 'POST', 'DELETE'])
def teachers(departament_id):
    teachers_schema = TeachersSchema(many=True)
    res = {}
    if request.method == 'GET':
        teachers_courses = query_db('SELECT t.id, c.id AS course_id FROM teachers AS t '
                                    'JOIN course AS c ON c.teacher_id = t.id '
                                    'WHERE departament_id=?', (departament_id,))

        teachers_data = query_db('SELECT * FROM teachers '
                                 'WHERE departament_id=?', (departament_id,))
        teachers_sch = teachers_schema.load(teachers_data)
        res = format_teachers(teachers_sch.data, teachers_courses)
    elif request.method == 'POST':
        teachers_sch = teachers_schema.loads(request.data)
        if not teachers_sch.errors:
            for t in teachers_sch.data:
                query_db('INSERT INTO teachers (name, gender, birth_date, phone_number, departament_id) '
                         'VALUES (?,?,?,?,?)',
                         (t.get('name'), t.get('gender'),
                          t.get('birth_date'), t.get('phone_number'),
                          departament_id))
            get_db().commit()
            res = 'Ok'
        else:
            res = teachers_sch.errors
    elif request.method == 'DELETE':
        id_sch = IdListSchema().loads(request.data)
        if not id_sch.errors:
            question_marks = ['?'] * len(id_sch.data['id_list'])
            query_db('delete from teachers where id in ({question_marks})'
                     .format(question_marks=','.join(question_marks)), id_sch.data['id_list'])
            get_db().commit()
            res = 'Ok'
        else:
            res = id_sch.errors
    return jsonify(res)


@teachers_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>',
                      methods=['GET', 'PUT', 'DELETE'])
def teacher(departament_id, teacher_id):
    res = {}
    if request.method == 'GET':
        courses_rel = query_db('SELECT t.id, c.id AS course_id FROM teachers AS t '
                               'JOIN course AS c ON c.teacher_id = t.id '
                               'WHERE t.id=? AND t.departament_id=?',
                               (teacher_id, departament_id))
        teacher_data = query_db('SELECT * FROM teachers WHERE id=? AND departament_id=?',
                                (teacher_id, departament_id))
        res = format_teachers(TeachersSchema(many=True).load(teacher_data).data, courses_rel)
    elif request.method == 'PUT':
        teacher_fields = TeachersSchema().loads(request.data)
        if not teacher_fields.errors:
            for field in teacher_fields.data:
                query_db('update teachers set {field_name}=? '
                         'where departament_id=? and id=?'
                         .format(field_name=field),
                         (teacher_fields.data[field], departament_id, teacher_id))
            get_db().commit()
            res = 'Ok'
        else:
            res = teacher_fields.errors
    elif request.method == 'DELETE':
        query_db('DELETE FROM teachers '
                 'WHERE id=? AND departament_id=?',
                 (teacher_id, departament_id))
        res = 'Ok'
    return jsonify(res)


@teachers_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>/courses',
                      methods=['GET'])
def teacher_courses(departament_id, teacher_id):
    courses_data = query_db('SELECT * FROM course AS c '
                            'JOIN teachers AS t ON c.teacher_id = t.id '
                            'JOIN departaments AS d ON t.departament_id = d.id '
                            'WHERE c.teacher_id=? AND d.id=?', (teacher_id, departament_id))
    return jsonify(CoursesSchema().load(courses_data))
