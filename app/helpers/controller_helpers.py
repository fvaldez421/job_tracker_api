


class ControllerHelpers:
    default_val = 'DEFAULT_VALUE'

    @staticmethod
    def checkForAnyUpdates(fields, updates):
        if updates != None:
            for key in fields:
                if updates.get(key, ControllerHelpers.default_val) != ControllerHelpers.default_val:
                    return True
        return False
    
    @staticmethod
    def checkForAllUpdates(fields, updates):
        if updates != None:
            for key in fields:
                if updates.get(key, ControllerHelpers.default_val) == ControllerHelpers.default_val:
                    return False
            return True
        return False