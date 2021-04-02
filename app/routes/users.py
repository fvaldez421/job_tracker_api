from flask import Blueprint, request

from app.database.models import User
from app.controllers.user_controller import UserController


users_bp = Blueprint('users', __name__)

# base users routes
# get (all)
# post (new users)
# deletes all users
@users_bp.route('/users', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return {
            "users": UserController.get_all_users()
        }

    if request.method == 'POST':
        req_body = request.json
        user = UserController.create_user(req_body)
        return {
            "user": user,
            "success": user != None
        }

    if request.method == 'DELETE':
        success = UserController.delete_all_users()
        return {
            "success": success
        }

# specific user routes
# get (single user)
# put (edit single user)
# delete (single user)
@users_bp.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_by_id(user_id=None):
    if request.method == 'GET':
        return {
            "users": User.objects(pk=user_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        user = UserController.update_user(user_id, req_body)
        return {
            "user": user,
            "success": user != None
        }
    if request.method == 'DELETE':
        user = UserController.delete_user(user_id)
        return {
            "user": user,
            "success": user != None
        }
