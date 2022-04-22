from flask import Response, json, jsonify
from src.models.option import Option
#from src.models.product import Product
#from src.services.product import Product

from src import db

"""[POST]"""


def create_option_service(data):
    try:
        """Get Data"""
        productID = data["productID"]
        ram = data["ram"]
        rom = data["rom"]
        price = data["price"]
        image = data["image"]
        colorID = data["colorID"]
        
        """Verify"""
        if (
            not productID
            or not ram
            or not rom
            or not price
            or not image
            or not colorID
        ):
            return jsonify({"code": 1, "message": "Missing required params"})
        """Handle data and return result"""

        """Hash image"""
        #hashed = hashpw(image.encode("utf-8"), gensalt())

        """ Create new option"""
        newoption = Option(productID, ram, rom, price, image,colorID)

        # Insert new option
        db.session.add(newoption)

        db.session.commit()
        return jsonify({"code": 0, "message": "option has created"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def formatOptions(optionsRaw):
    Options = []
    for item in optionsRaw.items:
       # print(item.genderData.value)
        Option = format_option(item)
        Options.append(Option)
    return Options

def format_productID(optionsRaw):
    Options = []
    for item in optionsRaw:
       # print(item.genderData.value)
        Option = format_option(item)
        Options.append(Option)
    return Options


def format_option(optionRaw):
    return {
        "id": optionRaw.id,
        "productID": optionRaw.productID,
        "ram": optionRaw.ram,
        "rom":optionRaw.rom,
        "price": optionRaw.price,
        "colorID": optionRaw.colorID,

    }


"""[GET]"""


def get_all_options_servive(data):
    try:
        page = data["page"] or "1"
        per_page = data["per_page"] or "10"
        """Check digit"""
        if not page.isdigit() or not per_page.isdigit():
            page = 1
            per_page = 10
        else:
            page = int(page)
            per_page = int(per_page)
        optionsRaw = Option.query.paginate(per_page=per_page, page=page, error_out=True)
        """Format data options"""
        options = formatOptions(optionsRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "options": options,
                    "per_page": optionsRaw.per_page,
                    "current_page": optionsRaw.page,
                    "total_pages": optionsRaw.pages,
                },
                "code": 0,
                "message": "Get all options success",
            }
        )
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Get all options fail"})


"""[DELETE]"""


def delete_option_service(optionId):
    try:
        """Check is digit"""
    
        response = find_option(optionId)
        if response["isExist"] and response["code"] == 0:
            db.session.delete(response["option"])
            db.session.commit()
            return jsonify({"code": 0, "message": "Delete option success"})
        return jsonify({"code": 1, "message": "Delete option failure"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


"""Find option"""


def find_option(id):
    try:
        option = Option.query.filter_by(id=id).first()
        if not option is None:
            return {"isExist": True, "option": option, "code": 0}
        else:
            return {"isExist": False, "code": 0}
    except Exception as e:
        print(e)
        return {"isExist": False, "code": 1}

"""Find productID"""

def find_productID(productID):
    try:
        option = Option.query.filter_by(productID=productID)
        #print(option)
        if not option is None:
            return {"isExist": True, "option": option, "code": 0}
        else:
            return {"isExist": False, "code": 0}
    except Exception as e:
        print(e)
        return {"isExist": False, "code": 1}



"""Update option [PUT]"""


def update_option_service(data):
    try:
        response = find_option(data["id"])
        if response["isExist"] and response["code"] == 0:
            option = response["option"]
            option.productID = data["productID"]
            option.ram = data["ram"]
            option.rom = data["rom"]
            option.price = data["price"]
            option.image = data["image"]
            option.colorID = data["colorID"]

            # Confirm update row
            db.session.commit()
            return jsonify({"code": 0, "message": "Update option success"})
        return jsonify({"code": 1, "message": "Update option fail"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})






"""Get option by id """


def get_option_by_id_service(productID):
    try:
        """Find productID"""
        response = find_productID(productID)
        #print(response)
        if response["isExist"] and response["code"] == 0:
            
            print(response["option"])
            #print("hello")
            option = format_productID(response["option"])
            return jsonify({"code": 0,"productID":productID, "option": option, "message": "Get option success"})
        return jsonify({"code": 1, "message": "Id invalid"})
    except Exception as e:
        print("service", e)
        return jsonify({"code": 2, "message": "Error from server"})