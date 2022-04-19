from src.services.user import (
    create_user_service,
    delete_user_service,
    get_all_users_servive,
    delete_user_service,
    get_user_by_id_service,
    update_user_service,
)

"""[POST]"""


def create_user_controller(data):
    return create_user_service(data)


"""[GET]"""


def get_all_users_controller(data):
    return get_all_users_servive(data)


"""[DELETE]"""


def delete_user_controller(id):
    return delete_user_service(id)


"""[GET]"""


def get_user_by_id_controller(id):
    return get_user_by_id_service(id)


"""[PUT] Update user"""


def update_user_controller(data):
    return update_user_service(data)
