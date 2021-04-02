from app.database.models import User



class UserController:
    @staticmethod
    def get_all_users():
        return User.objects

    @staticmethod
    def get_single_user(user_id=None):
        user = User.objects.get(pk=user_id)
        print(user)
        return user

    @staticmethod
    def create_user(user_data = None):
        user = None
        if 'name' in user_data and 'email' in user_data:
            user = User(
                name = user_data['name'],
                email = user_data['email']
            )
            user = user.save()
        return user

    @staticmethod
    def update_user(user_id = None, updates = None):
        user = None
        success = False
        print(user_id, updates)
        if user_id != None or updates != None:
            user = UserController.get_single_user(user_id=user_id)
            if user != None:
                if 'name' in updates: user.name = updates['name']
                if 'email' in updates: user.email = updates['email']
                user.save()
                success = True
        return success

    @staticmethod
    def delete_user(user_id = None):
        user = None
        success = False
        print(user_id)
        if user_id != None:
            user = UserController.get_single_user(user_id=user_id)
            if user != None:
                user.delete()
                success = True
        return success

    @staticmethod
    def delete_all_users():
        User.drop_collection()