from flask import Flask
from views import main_views

app = Flask(__name__)

app.register_blueprint(main_views)

app.config.from_object('app_config.DevConfig')


if __name__ == '__main__':
    app.run()



