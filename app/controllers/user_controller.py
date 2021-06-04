from app.database.models import User
from app.helpers.controller_helpers import ControllerHelpers
from app.helpers.date_helpers import DateHelpers

user_create_fields = [
    'name',
    'email'
]
user_update_fields = [
    'name',
    'email'
]

class UserController:
    @staticmethod
    def get_all_users():
        return User.objects

    @staticmethod
    def get_single_user(user_id=None):
        users = User.objects(pk=user_id)
        if len(users) > 0:
            return users[0]
        return None

    @staticmethod
    def create_user(user_data=None):
        user = None
        message = '"name" and "email" fields are required'
        valid_data = ControllerHelpers.checkForAllUpdates(user_create_fields, user_data)

        if valid_data:
            user_name = user_data['name'].strip()
            user_email = user_data['email'].strip()
            existing_user = User.objects(name__iexact=user_name)
            if existing_user:
                message = 'a user with that name and job "{}", "{}" already exists.'.format(user_name, user_email)
            else:
                user = User(
                    name=user_name,
                    email = user_email
                )
                user = user.save()
                message = 'successfully created user'
        return {
            'value': user,
            'success': True if user else False,
            'message': message
        }

    @staticmethod
    def update_user(user_id=None, updates=None):
        user = None
        message = 'can not update user with empty request body'
        success = False
        has_updates = ControllerHelpers.checkForAnyUpdates(user_update_fields, updates)
        if user_id != None and has_updates != None:
            user_name = updates.get('name')
            user_email = updates.get('email')
            user = UserController.get_single_user(user_id=user_id)
            if user == None:
                message = 'user with id "{}" not found'.format(user_id)
            else:
                if user_name:
                    user.name = user_name.strip()
                if user_email:
                    user.email = user_email.strip()
                
                user.save()
                success = True
                message = 'successfully updated user'
        return {
            'value': user,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_user(user_id=None):
        user = None
        success = False
        message = 'user with id "{}" not found'.format(user_id)
        if user_id != None:
            user = UserController.get_single_user(user_id=user_id)
            if user != None:
                user.delete()
                success = True
                message = 'successfully deleted user'
        return {
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_all_users():
        User.drop_collection()