from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
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
        teachers_courses = query_db('select t.id, c.id as course_id from teachers as t '
                                    'join course as c on c.teacher_id = t.id '
                                    'where departament_id=?', (departament_id,))

        teachers_data = query_db('select * from teachers '
                                 'where departament_id=?', (departament_id,))
        teachers_sch = teachers_schema.load(teachers_data)
        res = format_teachers(teachers_sch.data, teachers_courses)
    elif request.method == 'POST':
        teachers_sch = teachers_schema.loads(request.data)
        if not teachers_sch.errors:
            for t in teachers_sch.data:
                query_db('insert into teachers (name, gender, birth_date, phone_number, departament_id) '
                         'values (?,?,?,?,?)',
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
            question_marks = ['?']*len(id_sch.data['id_list'])
            query_db('delete from teachers where id in (quesion_marks)'
                     .format(question_marks=','.join(question_marks)), id_sch.data['id_list'])
            get_db().commit()
            res = 'Ok'
        else:
            res = id_sch.errors
    return jsonify(res)


@teachers_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>')
def teacher(departament_id, teacher_id):
    teacher = query_db('select t.*, c.id as course_id from teachers as t '
                       'join course as c on c.teacher_id = t.id '
                       'where t.id={teacher_id}'
                       .format(teacher_id=teacher_id))
    res = format_teachers(teacher)
    return jsonify(res)


@teachers_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>/courses')
def teacher_courses(departament_id, teacher_id):
    courses = query_db('select * from course '
                       'where teacher_id={teacher_id}'
                       .format(teacher_id=teacher_id))
    return jsonify(courses)