from flask_cors import CORS, cross_origin


def config_app(app):
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["SECRET_KEY"] = "dev"
