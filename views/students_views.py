import os
from datetime import datetime

from flask import Blueprint, jsonify, request, send_from_directory

from db_utils import query_db, get_db
from schemas.general import IdListSchema
from schemas.students import StudentsSchema
from utils import calculate_age
from report_writer import ReportWriter
from app_config import STUDENT_REPORT

students_views = Blueprint('students_views', __name__)


@students_views.route('/students',
                      methods=['GET', 'POST', 'DELETE'])
def students():
    student_schema = StudentsSchema(many=True)
    if request.method == 'GET':
        query_res = query_db('SELECT s.* FROM students AS s '
                             'JOIN groups AS g ON s.group_id = g.id '
                             'JOIN departaments AS d ON g.departament_id = d.id')
        res = student_schema.load(query_res).data
        return jsonify(res)
    elif request.method == 'POST':
        # TODO валидация
        student_schema = StudentsSchema(many=True).loads(request.data)
        if not student_schema.errors:
            student_data = student_schema.data
            res = 'Ok'
            for s in student_data:
                query_db("INSERT INTO students (name, gender, birth_date, phone_number, group_id) "
                         "VALUES (?,?,?,?,?)", (s['name'], s['gender'],
                                                s.get('birth_date'), s.get('phone_number'),
                                                s.get('group_id')))
            get_db().commit()
        else:
            res = student_schema.errors
        return jsonify(res)
    elif request.method == 'DELETE':
        # TODO добавить детальную обработку запроса (вывод информации о удалении, либо об отсутствии студентов
        # TODO с таким id)
        id_schema = IdListSchema().loads(request.data)
        if not id_schema.errors:
            question_marks = ['?'] * (len(id_schema.data['id_list']))
            res = query_db("delete from students where id in ({question_marks});"
                           .format(question_marks=','.join(question_marks)), id_schema.data['id_list'])
            get_db().commit()
        else:
            res = id_schema.errors
        return jsonify(res)


@students_views.route('/students/view')
def students_view():
    students_data = query_db('select s.id, s.name, g.name as group_name, g.course, '
                             's.gender, s.birth_date, s.phone_number, d.name as departament_name '
                             'from students as s '
                             'join groups as g on s.group_id = g.id '
                             'join departaments as d on d.id = g.departament_id')
    students_sch = StudentsSchema(many=True).load(students_data).data
    for s in students_sch:
        birth_date = datetime.strptime(s.pop('birth_date'), '%Y-%m-%d')
        s['age'] = calculate_age(birth_date)
        return jsonify(students_sch)


@students_views.route('/students/<int:student_id>',
                      methods=['GET', 'PUT', 'DELETE'])
def student(student_id):
    if request.method == 'GET':
        res = query_db('SELECT s.* FROM students AS s '
                       'JOIN groups AS g ON s.group_id = g.id '
                       'JOIN departaments AS d ON g.departament_id = d.id '
                       'WHERE s.id=?', (student_id,))
        return jsonify(res)
    elif request.method == 'PUT':
        student_schema = StudentsSchema(field_requirement=False).loads(request.data)
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
        query_db("DELETE FROM students WHERE id=?;", (student_id,))
        get_db().commit()
        return jsonify('Ok')


@students_views.route('/students/<int:student_id>/report',
                      methods=['GET', 'PUT', 'DELETE'])
def student_report_one(student_id):
    student_courses_data = query_db('select s.name, g.name as group_name, '
                                    'c.name as course_name, t.name as teacher_name, '
                                    'c.duration as duration '
                                    'from students as s '
                                    'join groups as g on s.group_id = g.id '
                                    'join course as c on g.id = c.group_id '
                                    'join teachers as t on c.teacher_id = t.id '
                                    'join departaments as d on g.departament_id = d.id '
                                    'where s.id=?',
                                    (student_id,))

    if len(student_courses_data) > 0:
        ReportWriter(report_type=STUDENT_REPORT).make_report({'headings': list(student_courses_data[0].keys()),
                                                              'report_data': student_courses_data})
        return send_from_directory(os.path.join(os.path.curdir, 'reports'),
                                   'report_1.xlsx',
                                   as_attachment=True)
    else:
        return jsonify('Something wrong happened', status=403)
