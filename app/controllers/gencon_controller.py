from app.database.models import GeneralContractor
from app.helpers.controller_helpers import ControllerHelpers
from app.helpers.date_helpers import DateHelpers

gencon_create_fields = [
    'name'
]
gencon_update_fields = [
    'name'
]

class GeneralContractorController:
    @staticmethod
    def get_all_generalcontractors():
        return GeneralContractor.objects

    @staticmethod
    def find_by_id(generalcontractor_id=None):
        generalcontractors = GeneralContractor.objects(pk=generalcontractor_id)
        if len(generalcontractors) > 0:
            return generalcontractors[0]
        return None
        

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return GeneralContractor.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_generalcontractor(generalcontractor_data=None):
        generalcontractor = None
        message = '"name" is a required field'
        valid_data = ControllerHelpers.checkForAllUpdates(gencon_create_fields, generalcontractor_data)
        if valid_data:
            generalcontractor_name = generalcontractor_data['name'].strip()
            mod_id = generalcontractor_data.get('mod_id')
            existing_generalcontractor = GeneralContractor.objects(name__iexact=generalcontractor_name)
            if existing_generalcontractor:
                message = 'a general contractor with that name "{}" already exists'.format()
            else:
                generalcontractor = GeneralContractor(
                    name=generalcontractor_name,
                    created_by=mod_id
                )
                generalcontractor = generalcontractor.save()
                message = 'successfully created general contractor'
        return {
            'value': generalcontractor,
            'success': True if generalcontractor else False,
            'message': message
        }

    @staticmethod
    def update_generalcontractor(generalcontractor_id=None, updates=None):
        generalcontractor = None
        success = False
        message = 'can not update general contractor with empty body'
        has_updates = ControllerHelpers.checkForAnyUpdates(gencon_update_fields, updates)
        if generalcontractor_id != None or updates != None:
            mod_id = updates.get('mod_id')
            generalcontractor_name = updates.get('name')
            if generalcontractor_name or mod_id:
                generalcontractor = GeneralContractorController.find_by_id(generalcontractor_id=generalcontractor_id)
                if generalcontractor != None:
                    message = 'general contractor with id "{}" not found'.format(generalcontractor_id)
                    if generalcontractor_name:
                        generalcontractor.name = generalcontractor_name.strip()
                    if mod_id:
                        generalcontractor.modified_by = mod_id
                    generalcontractor.save()
                    success = True
                    message = 'successfully updated general contractor'
        return {
            'value': generalcontractor,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_generalcontractor(generalcontractor_id=None):
        generalcontractor = None
        success = False
        message = 'general contractor with id "{}" not found'.format(generalcontractor_id)
        if generalcontractor_id != None:
            generalcontractor = GeneralContractorController.find_by_id(generalcontractor_id=generalcontractor_id)
            if generalcontractor != None:
                generalcontractor.delete()
                success = True
                message = 'successfully deleted general contractor'
        return {
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_all_generalcontractors():
        GeneralContractor.drop_collection()
