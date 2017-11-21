import json
from flask import Blueprint, jsonify, request

from db_utils import query_db
from schemas.student import StudentSchema

students_views = Blueprint('students_views', __name__)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students', methods=['GET', 'POST'])
def students(departament_id, group_id):
    if request.method == 'GET':
        students = query_db('select * from students '
                            'where group_id={group_id}'.format(group_id=group_id))
        return jsonify(students)
    elif request.method == 'POST':
        rd = json.loads(request.data)
        schema = StudentSchema()
        res = schema.load(rd)
        print(rd)
        return jsonify(rd)


@students_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/students/<int:student_id>')
def student(departament_id, group_id, student_id):
    student = query_db('select * from students '
                       'where group_id={group_id} and id={student_id}'
                       .format(group_id=group_id, student_id=student_id))
    return jsonify(student)
