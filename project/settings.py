import flask
import flask_sqlalchemy
import flask_migrate
import os

python_app = flask.Flask(
    import_name = "project",
    instance_path = os.path.abspath(__file__ + "/..")
)

python_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = python_app)

migrate = flask_migrate.Migrate(app = python_app, db = DATABASE)