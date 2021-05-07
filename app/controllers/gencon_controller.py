from app.database.models import GeneralContractor


class GeneralContractorController:
    @staticmethod
    def get_all_generalcontractors():
        return GeneralContractor.objects

    @staticmethod
    def find_by_id(generalcontractor_id=None):
        generalcontractor = GeneralContractor.objects.get(pk=generalcontractor_id)
        return generalcontractor

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return GeneralContractor.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_generalcontractor(generalcontractor_data=None):
        generalcontractor = None
        if 'name' in generalcontractor_data:
            generalcontractor_name = generalcontractor_data['name'].strip()
            mod_id = generalcontractor_data.get('mod_id')
            existing_generalcontractor = GeneralContractor.objects(name__iexact=generalcontractor_name)
            if not existing_generalcontractor:
                generalcontractor = GeneralContractor(
                    name=generalcontractor_name,
                    created_by=mod_id
                )
                generalcontractor = generalcontractor.save()
        return generalcontractor

    @staticmethod
    def update_generalcontractor(generalcontractor_id=None, updates=None):
        generalcontractor = None
        success = False
        if generalcontractor_id != None or updates != None:
            mod_id = updates.get('mod_id')
            generalcontractor_name = updates.get('name')
            if generalcontractor_name or mod_id:
                generalcontractor = GeneralContractorController.find_by_id(generalcontractor_id=generalcontractor_id)
                if generalcontractor != None:
                    if generalcontractor_name:
                        generalcontractor.name = generalcontractor_name.strip()
                    if mod_id:
                        generalcontractor.modified_by = mod_id
                    generalcontractor.save()
                    success = True
        return generalcontractor if success else None

    @staticmethod
    def delete_generalcontractor(generalcontractor_id=None):
        generalcontractor = None
        success = False
        if generalcontractor_id != None:
            generalcontractor = GeneralContractorController.find_by_id(generalcontractor_id=generalcontractor_id)
            if generalcontractor != None:
                generalcontractor.delete()
                success = True
        return success

    @staticmethod
    def delete_all_generalcontractors():
        GeneralContractor.drop_collection()
