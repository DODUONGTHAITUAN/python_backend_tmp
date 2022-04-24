def get_data_json(data):
    return {
        "userID": data["userID"] or 1,
        "statusID": data["statusID"] or "STA1",
        "address": data["address"],
        "totalPrice": data["totalPrice"] or 0,
    }


def format_orders(data):
    return [format_order(item) for item in data]


def format_order(data):
    return {
        "id": data["id"],
        "userID": data["userID"],
        "statusID": data["statusID"],
        "address": data["address"],
        "totalPrice": data["totalPrice"],
    }
