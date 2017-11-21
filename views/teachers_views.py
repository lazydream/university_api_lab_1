from flask import Blueprint, jsonify

from db_utils import query_db
from utils import format_teachers

teachers_views = Blueprint('teachers_views', __name__)


@teachers_views.route('/departaments/<int:departament_id>/teachers')
def teachers(departament_id):
    teachers = query_db('select t.*, c.id as course_id from teachers as t '
                        'join course as c on c.teacher_id = t.id '
                        'where departament_id={departament_id}'.format(departament_id=departament_id))

    res = format_teachers(teachers)
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