import os
from flask import Flask, g, render_template
from views.courses_views import courses_views
from views.departaments_views import departaments_views
from views.groups_views import groups_views
from views.students_views import students_views
from views.teachers_views import teachers_views


template_dir = os.path.dirname(__file__)
template_dir = os.path.join(template_dir, 'client/public')

app = Flask(__name__, template_folder=template_dir)

app.register_blueprint(courses_views, url_prefix='/api')
app.register_blueprint(departaments_views, url_prefix='/api')
app.register_blueprint(groups_views, url_prefix='/api')
app.register_blueprint(students_views, url_prefix='/api')
app.register_blueprint(teachers_views, url_prefix='/api')


@app.route('/')
def render_page():
    return render_template('index.html')


@app.errorhandler(404)
def client__error_handler(error):
    return render_template('index.html'), 200


app.config.from_object('app_config.DevConfig')


@app.teardown_appcontext
def close_connection(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()

