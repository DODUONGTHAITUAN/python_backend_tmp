from os import environ

SQLALCHEMY_DATABASE_URI = str(environ.get("SQLALCHEMY_DATABASE_URI"))
DB_NAME = str(environ.get("DB_NAME"))
URL = SQLALCHEMY_DATABASE_URI + "/" + DB_NAME


def config_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/demo"
    # app.config["SQLALCHEMY_DATABASE_URI"] = URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
