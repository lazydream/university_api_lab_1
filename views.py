from flask import request, Blueprint, g
import sqlite3

main_views = Blueprint('main_views', __name__)


@main_views.route('/')
def hello_world():
    return 'hello, world'


@main_views.route('/user/<username>')
def username(username):
    return "User: {username}".format(username=username)


@main_views.route('/post/<int:post_id>')
def get_post(post_id):
    return "Post id: {id}".format(id=post_id)


@main_views.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        return 'You are POSTing me 8)'
    elif request.method == 'GET':
        return 'You are GETting me ^_^'


@main_views.route('/checkdb')
def check_db():
    database = './lab1.db'
    db = g._database = sqlite3.connect(database)
    cur = db.cursor()
    print(cur)
    return 'Ok'
