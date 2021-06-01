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
        text_query = request.args.get('q', None)
        users = None
        if text_query != None:
            users = UserController.find_by_name(text_query)
        else:
            users = UserController.get_all_users()
        return {
            "users": users
        }

    if request.method == 'POST':
        req_body = request.json
        res = UserController.create_user(req_body)
        return {
            'user': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }

    if request.method == 'DELETE':
        success = UserController.delete_all_users()
        return {
            "success": success
        }
        
#@users_bp.route('/users', methods=['GET', 'POST', 'DELETE'])
#def index():
#    if request.method == 'GET':
#        return {
#            "users": UserController.get_all_users()
#        }
#
#    if request.method == 'POST':
#        req_body = request.json
#        user = UserController.create_user(req_body)
#        return {
#            "user": user,
#            "success": user != None
#        }

#    if request.method == 'DELETE':
#        success = UserController.delete_all_users()
#        return {
#            "success": success
#        }

# specific user routes
# get (single user)
# put (edit single user)
# delete (single user)
@users_bp.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_by_id(user_id=None):
    if request.method == 'GET':
        message = 'user not found'
        user = UserController.find_by_id(user_id)
        return {
            'user': user,
            'success': True if user else False,
            'message': None if user else message
        }
    if request.method == 'PUT':
        req_body = request.json
        res = UserController.update_user(user_id, req_body)
        return {
            'user': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }
    if request.method == 'DELETE':
        res = UserController.delete_user(user_id)
        return {
            'success': res.get('success', False),
            'message': res.get('message')

#@users_bp.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
#def user_by_id(user_id=None):
#    if request.method == 'GET':
 #       return {
  #          "users": User.objects(pk=user_id)
   #     }
    #if request.method == 'PUT':
#        req_body = request.json
#        user = UserController.update_user(user_id, req_body)
 #       return {
  #          "user": user,
   #         "success": user != None
    #    }
    #if request.method == 'DELETE':
    #    user = UserController.delete_user(user_id)
    #    return {
    #        "user": user,
    #        "success": user != None
    #    }
