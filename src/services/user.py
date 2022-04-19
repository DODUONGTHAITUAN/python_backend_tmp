from flask import Response, json, jsonify
from bcrypt import hashpw, checkpw, gensalt
from src.models.user import User

from src import db

"""[POST]"""


def create_user_service(data):
    try:
        """Get Data"""
        fullName = data["fullName"]
        address = data["address"]
        email = data["email"]
        phonenumber = data["phonenumber"]
        password = data["password"]
        genderID = data["genderID"]
        roleID = data["roleID"]
        """Verify"""
        if (
            not fullName
            or not address
            or not email
            or not phonenumber
            or not password
            or not genderID
            or not roleID
        ):
            return jsonify({"code": 1, "message": "Missing required params"})
        """Handle data and return result"""

        """Hash password"""
        hashed = hashpw(password.encode("utf-8"), gensalt())

        """ Create new User"""
        newUser = User(fullName, genderID, address, phonenumber, email, hashed, roleID)

        # Insert new user
        db.session.add(newUser)
        db.session.commit()
        return jsonify({"code": 0, "message": "user has created"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def formatUsers(usersRaw):
    users = []
    for item in usersRaw.items:
        print(item.genderData.value)
        user = format_user(item)
        users.append(user)
    return users


def format_user(userRaw):
    return {
        "id": userRaw.id,
        "fullName": userRaw.fullName,
        "genderID": userRaw.genderID,
        "address": userRaw.address,
        "phonenumber": userRaw.phonenumber,
        "email": userRaw.email,
        "roleID": userRaw.roleID,
        "gender_value": userRaw.genderData.value,
        "role_value": userRaw.roleData.value,
    }


"""[GET]"""


def get_all_users_servive(data):
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
        usersRaw = User.query.paginate(per_page=per_page, page=page, error_out=True)
        """Format data users"""
        users = formatUsers(usersRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "users": users,
                    "per_page": usersRaw.per_page,
                    "current_page": usersRaw.page,
                    "total_pages": usersRaw.pages,
                },
                "code": 0,
                "message": "Get all users success",
            }
        )
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Get all users fail"})


"""[DELETE]"""


def delete_user_service(userId):
    try:
        """Check is digit"""
        response = find_user(userId)
        if response["isExist"] and response["code"] == 0:
            db.session.delete(response["user"])
            db.session.commit()
            return jsonify({"code": 0, "message": "Delete user success"})
        return jsonify({"code": 1, "message": "Delete user failure"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


"""Find user"""


def find_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user is None:
            return {"isExist": True, "user": user, "code": 0}
        else:
            return {"isExist": False, "code": 0}
    except Exception as e:
        print(e)
        return {"isExist": False, "code": 1}


"""Update user [PUT]"""


def update_user_service(data):
    try:
        response = find_user(data["id"])
        if response["isExist"] and response["code"] == 0:
            user = response["user"]
            user.fullName = data["fullName"]
            user.address = data["address"]
            user.phonenumber = data["phonenumber"]
            user.email = data["email"]
            user.roleID = data["roleID"]

            # Confirm update row
            db.session.commit()
            return jsonify({"code": 0, "message": "Update user success"})
        return jsonify({"code": 1, "message": "Update user fail"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


"""Change passaword"""


def update_password_user(data):
    try:
        id = data["id"]
        password = data["password"]
        newPassword = data["newPassword"]
        response = find_user(id)
        if response["isexist"] and response["code"] == 0:
            if compare_password(password, response["user"].password):
                """Hash password"""
                hashed = hashpw(password.encode("utf-8"), gensalt())
                response["user"].password = hashed
                db.session.commit()
                return jsonify({"code": 0, "message": "Change password success"})
            return jsonify({"code": 1, "message": "Password invalid"})
        return jsonify({"code": 2, "message": "User invalid"})
    except Exception as e:
        print(e)
        return jsonify({"code": 3, "message": "Error from server"})


"""Check user.password match password in database"""


def compare_password(paswwordFromClient, passwordUser):
    if checkpw(paswwordFromClient.encode("utf-8"), passwordUser):
        return True
    else:
        return False


"""Get user by id """


def get_user_by_id_service(id):
    try:
        """Find user"""
        response = find_user(id)
        if response["isExist"] and response["code"] == 0:
            print(response["user"].fullName)
            user = format_user(response["user"])
            return jsonify({"code": 0, "user": user, "message": "Get user success"})
        return jsonify({"code": 1, "message": "Id invalid"})
    except Exception as e:
        print("service", e)
        return jsonify({"code": 2, "message": "Error from server"})
