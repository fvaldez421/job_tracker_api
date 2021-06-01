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
        user = User.objects.get(pk=user_id)
        return user

    @staticmethod
    def create_user(user_data=None):
        user = None
        message = '"name" and "email" fields are required'
        valid_data = ControllerHelpers.checkForAllUpdates(user_create_fields, user_data)

        if valid_data:
            user_name = user_data['name'].strip()
            user_email = user_data['email'].strip()
            mod_id = user_data.get('mod_id')
            existing_user = User.objects(name__iexact=user_name)
            if existing_user:
                message = 'a user with that name and job "{}", "{}" already exists.'.format(user_name, user_email)
            else:
                user = User(
                    name=user_name,
                    email = user_email,
                    created_by=mod_id
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
        print(has_updates)
        if user_id != None and has_updates != None:
            mod_id = updates.get('mod_id')
            email = updates.get('email')
            user_name = updates.get('name')
            user = UserController.find_by_id(user_id=user_id)
            if user == None:
                message = 'user with id "{}" not found'
            else:
                if user_name:
                    user.name = user_name.strip()
                if user_email:
                    user.email = user_email.strip()
                if mod_id:
                    user.modified_by = mod_id
                
                user.save()
                success = True
                message = 'successfully updated user'
        return {
            'value': user,
            'success': success,
            'message': message
        }
    @staticmethod
    def update_user(user_id = None, updates = None):
        user = None
        success = False
        if user_id != None or updates != None:
            user = UserController.get_single_user(user_id=user_id)
            if user != None:
                if 'name' in updates: user.name = updates['name'].strip()
                if 'email' in updates: user.email = updates['email'].strip()
                user.save()
                success = True
        return success

    @staticmethod
    def delete_user(user_id=None):
        user = None
        success = False
        message = 'user with id "{}" not found'.format(user_id)
        if user_id != None:
            user = UserController.find_by_id(user_id=user_id)
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