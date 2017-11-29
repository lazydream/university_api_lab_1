from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
from schemas.courses import CoursesSchema
from schemas.general import IdListSchema

courses_views = Blueprint('courses_views', __name__)


@courses_views.route('/courses',
                     methods=['GET', 'POST', 'DELETE'])
def courses():
    courses_sch = CoursesSchema(many=True)
    res = {}
    if request.method == 'GET':
        courses_data = query_db('SELECT * FROM course ')
        res = courses_sch.load(courses_data).data
    elif request.method == 'POST':
        courses_list = courses_sch.loads(request.data)
        if not courses_list.errors:
            for new_course in courses_list.data:
                query_db('INSERT INTO course (id, name, teacher_id, group_id, semester, duration) '
                         'VALUES (?,?,?,?,?,?)', (new_course.get('id'), new_course.get('name'),
                                                  new_course.get('teacher_id'), new_course.get('group_id'),
                                                  new_course.get('semester'), new_course.get('duration')))
            get_db().commit()
            res = 'Ok'
        else:
            res = courses_list.errors
    elif request.method == 'DELETE':
        id_list = IdListSchema().loads(request.data)
        if not id_list.errors:
            question_marks = ['?'] * len(id_list.data)
            query_db('delete from course '
                     'where id in ({question_marks}) '
                     .format(question_marks=','.join(question_marks)),
                     id_list.data['id_list'])
            get_db().commit()
            res = 'Ok'
        else:
            res = id_list.errors
    return jsonify(res)


@courses_views.route('/courses/view', methods=['GET'])
def courses_view():
    courses_data = query_db('SELECT c.id, c.name, g.name AS group_name, '
                            'd.name AS departament_name, d.institute, '
                            'g.course, c.semester, t.name AS teacher_name, '
                            'c.duration FROM course AS c '
                            'JOIN groups AS g ON c.group_id = g.id '
                            'JOIN teachers AS t ON c.teacher_id = t.id '
                            'JOIN departaments AS d ON g.departament_id = d.id ')
    course_sch = CoursesSchema(many=True).load(courses_data).data
    return jsonify(course_sch)


@courses_views.route('/courses/<int:course_id>',
                     methods=['GET', 'PUT', 'DELETE'])
def course(course_id):
    res = {}
    if request.method == 'GET':
        course_data = query_db('select * from course where id={course_id}'.format(course_id=course_id))
        res = CoursesSchema(many=True).load(course_data).data
    elif request.method == 'PUT':
        fields = CoursesSchema().loads(request.data)
        if not fields.errors:
            for field in fields.data:
                query_db('update course set {field_name}=?'
                         .format(field_name=field),
                         (fields.data[field],))
            get_db().commit()
            res = 'Ok'
        else:
            res = fields.errors
    elif request.method == 'DELETE':
        query_db('DELETE FROM course WHERE id=?', (course_id,))
        get_db().commit()
        res = 'Ok'
    return jsonify(res)

