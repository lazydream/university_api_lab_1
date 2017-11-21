from flask import Flask, g
from views.courses_views import courses_views
from views.departaments_views import departaments_views
from views.groups_views import groups_views
from views.students_views import students_views
from views.teachers_views import teachers_views

app = Flask(__name__)

app.register_blueprint(courses_views)
app.register_blueprint(departaments_views)
app.register_blueprint(groups_views)
app.register_blueprint(students_views)
app.register_blueprint(teachers_views)

app.config.from_object('app_config.DevConfig')


@app.teardown_appcontext
def close_connection(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()

