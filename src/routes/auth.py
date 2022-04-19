from flask import Blueprint, request
from src.ultils.constants import methods, path

from src.controllers.auth_controller import get_current_user_controller

auth = Blueprint("auth", __name__)


@auth.route(path["LOGIN"], methods=["POST", "GET"])
def login():
    if request.method == methods["GET"]:
        pass
    elif request.method == methods["POST"]:
        data = request.get_json()
    return get_current_user_controller(data)


@auth.route("/register")
def register():
    return "<h1>Hello world Register Page</h1>"
