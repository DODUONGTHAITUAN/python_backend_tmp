from src.services.product import get_all_products_service


def get_all_products_controller(data):
    return get_all_products_service(data)
