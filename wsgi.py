app = Flask(__name__)

app.register_blueprint(courses_views)
app.register_blueprint(departaments_views)
app.register_blueprint(groups_views)
app.register_blueprint(students_views)
app.register_blueprint(teachers_views)

app.config.from_object('app_config.DevConfig')