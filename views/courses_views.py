from flask import Blueprint, jsonify

from db_utils import query_db

courses_views = Blueprint('course_views', __name__)


@courses_views.route('/courses')
def courses():
    courses = query_db('select * from course ')
    return jsonify(courses)


@courses_views.route('/courses/<int:course_id>')
def course(course_id):
    course = query_db('select * from course where id={course_id}'.format(course_id=course_id))
    return jsonify(course)