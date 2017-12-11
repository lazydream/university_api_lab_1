from flask import Blueprint, jsonify, request

from db_utils import query_db, get_db
from schemas.general import IdListSchema
from schemas.groups import GroupsSchema
from utils import format_groups

groups_views = Blueprint('groups_views', __name__)


@groups_views.route('/groups',
                    methods=['GET', 'POST', 'DELETE'])
def groups():
    groups_schema = GroupsSchema(many=True)
    res = {}
    if request.method == "GET":
        groups_res = query_db('select * from groups ')
        groups_sch = groups_schema.load(groups_res)
        res = format_groups(groups_sch.data)
    elif request.method == "POST":
        groups_data = groups_schema.loads(request.data)
        if not groups_data.errors:
            for new_group in groups_data.data:
                query_db('INSERT INTO groups (name, departament_id) VALUES (?,?)',
                         (new_group['name'], new_group['departament_id']))
                res = 'Ok'
            get_db().commit()
        else:
            res = groups_data.errors
    elif request.method == "DELETE":
        id_schema = IdListSchema().loads(request.data)
        if not id_schema.errors:
            res = 'Ok'
            question_marks = ['?'] * (len(id_schema.data['id_list']))
            query_db('delete from groups where id in ({question_marks})'
                     .format(question_marks=','.join(question_marks)), id_schema.data['id_list'])
            get_db().commit()
        else:
            res = id_schema.errors
    return jsonify(res)


@groups_views.route('/groups/<int:group_id>',
                    methods=['GET', 'PUT', 'DELETE'])
def group(group_id):
    if request.method == 'GET':
        group_data = query_db('select * from groups '
                              'and id=?', (group_id,))
        res = format_groups(GroupsSchema().load(group_data).data)
    elif request.method == 'PUT':
        group_schema = GroupsSchema().loads(request.data)
        if not group_schema.errors:
            for g in group_schema.data:
                query_db('update groups set {field_name}=? where id=?'
                         .format(field_name=g),
                         (group_schema.data[g], group_id,))
            get_db().commit()
            res = 'Ok'
        else:
            res = group_schema.errors
    return jsonify(res)


@groups_views.route('groups/<int:group_id>/courses')
def group_courses(group_id):
    courses = query_db('select * from course '
                       'where group_id={group_id}'
                       .format(group_id=group_id))
    return jsonify(courses)
