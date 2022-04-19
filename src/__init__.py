from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from .routes import routes
from .configs import config_app
from .configs.configDB import config_db


app = Flask(__name__)
db = SQLAlchemy(app)

from .models.allcodes import Allcodes
from .models.user import User
from .models.product import Product
from .models.option import Option
from .models.detail_product import DetailProduct


def create_app():
    """Config app"""
    config_app(app)

    """Routes app"""
    routes(app)

    """Config database app"""
    config_db(app)
    db.init_app(app)

    db.create_all()

    return app
