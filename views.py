from flask import request, Blueprint, g, jsonify
from flask.helpers import url_for

from db_utils import query_db
from utils import format_departaments, format_groups, format_teachers

main_views = Blueprint('main_views', __name__)


@main_views.route('/departaments')
def departaments():
    departaments = query_db('select * from departaments')
    res = format_departaments(departaments)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>')
def departament(departament_id):
    departament = query_db('select * from departaments '
                           'where id={departament_id}'
                           .format(departament_id=departament_id))
    res = format_departaments(departament)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>/teachers')
def teachers(departament_id):
    teachers = query_db('select t.*, c.id as course_id from teachers as t '
                        'join course as c on c.teacher_id = t.id '
                        'where departament_id={departament_id}'.format(departament_id=departament_id))

    res = format_teachers(teachers)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>')
def teacher(departament_id, teacher_id):
    teacher = query_db('select t.*, c.id as course_id from teachers as t '
                       'join course as c on c.teacher_id = t.id '
                       'where t.id={teacher_id}'
                       .format(teacher_id=teacher_id))
    res = format_teachers(teacher)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>/teachers/<int:teacher_id>/courses')
def teacher_courses(departament_id, teacher_id):
    courses = query_db('select * from course '
                       'where teacher_id={teacher_id}'
                       .format(teacher_id=teacher_id))
    return jsonify(courses)


@main_views.route('/departaments/<int:departament_id>/groups')
def groups(departament_id):
    groups = query_db('select g.*, c.id from groups as g '
                      'join course as c on c.group_id = g.id '
                      'where g.departament_id={departament_id}'
                      .format(departament_id=departament_id))
    res = format_groups(groups)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>/groups/<int:group_id>')
def group(departament_id, group_id):
    group = query_db('select * from groups '
                     'where departament_id={departament_id} '
                     'and id={group_id}'
                     .format(departament_id=departament_id, group_id=group_id))
    res = format_groups(group)
    return jsonify(res)


@main_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/courses')
def group_courses(departament_id, group_id):
    courses = query_db('select * from course '
                       'where group_id={group_id}'
                       .format(group_id=group_id))
    return jsonify(courses)


@main_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students')
def students(departament_id, group_id):
    students = query_db('select * from students '
                        'where group_id={group_id}'.format(group_id=group_id))
    return jsonify(students)


@main_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students/<int:student_id>')
def student(departament_id, group_id, student_id):
    student = query_db('select * from students '
                       'where group_id={group_id} and id={student_id}'
                       .format(group_id=group_id, student_id=student_id))
    return jsonify(student)


@main_views.route('/courses')
def courses():
    courses = query_db('select * from course ')
    return jsonify(courses)


@main_views.route('/courses/<int:course_id>')
def course(course_id):
    course = query_db('select * from course where id={course_id}'.format(course_id=course_id))
    return jsonify(course)



