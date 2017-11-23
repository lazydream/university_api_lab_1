import json, unicodedata
from flask import Blueprint, jsonify, request

from db_utils import query_db
from schemas.student import StudentSchema

students_views = Blueprint('students_views', __name__)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students', methods=['GET', 'POST'])
def students(departament_id, group_id):
    schema = StudentSchema(many=True)

    if request.method == 'GET':
        students = query_db('select * from students '
                            'where group_id={group_id}'.format(group_id=group_id))
        res = schema.dumps(students, ensure_ascii=False)
        return jsonify(res.data)
    elif request.method == 'POST':
        rd = json.loads(request.data)
        res = schema.load(rd)
        print(rd)

        insert_res = query_db('insert into students (name, gender, birth_date, phone_number, group_id) '
                              'values ({name}, {gender}, {birth_date}, {phone_number}, {group_id})'
                              .format(name=rd['name'], gender=rd['gender'],
                                      birth_date=rd['birth_date'], phone_number=rd['phone_number'],
                                      group_id=rd['group_id']))

        return jsonify(rd)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students/<int:student_id>')
def student(departament_id, group_id, student_id):
    student = query_db('select * from students '
                       'where group_id={group_id} and id={student_id}'
                       .format(group_id=group_id, student_id=student_id))
    return jsonify(student)
