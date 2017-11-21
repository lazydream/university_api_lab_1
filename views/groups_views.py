from flask import Blueprint, jsonify

from db_utils import query_db
from utils import format_groups

groups_views = Blueprint('groups_views', __name__)


@groups_views.route('/departaments/<int:departament_id>/groups')
def groups(departament_id):
    groups = query_db('select * from groups '
                      'where departament_id={departament_id}'
                      .format(departament_id=departament_id))
    res = format_groups(groups)
    return jsonify(res)


@groups_views.route('/departaments/<int:departament_id>/groups/<int:group_id>')
def group(departament_id, group_id):
    group = query_db('select * from groups '
                     'where departament_id={departament_id} '
                     'and id={group_id}'
                     .format(departament_id=departament_id, group_id=group_id))
    res = format_groups(group)
    return jsonify(res)


@groups_views.route('/departaments/<int:departament_id>/groups/<int:group_id>/courses')
def group_courses(departament_id, group_id):
    courses = query_db('select * from course '
                       'where group_id={group_id}'
                       .format(group_id=group_id))
    return jsonify(courses)