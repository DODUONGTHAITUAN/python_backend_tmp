from flask import Blueprint, request

from src import db
from src.models.product import Product
from src.controllers.product import get_all_products_controller


product = Blueprint("product", __name__)


@product.route("/get-products")
def get_all_product():
    try:
        data = request.args.to_dict(flat=True)
        return get_all_products_controller(data)
    except Exception as e:
        print(e)
        return "Hello world"
