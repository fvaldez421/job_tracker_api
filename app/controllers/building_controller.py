from app.database.models import Building
from app.helpers.controller_helpers import ControllerHelpers
from app.helpers.date_helpers import DateHelpers


building_create_fields = [
    'name',
    'job',
]
building_update_fields = [
    'name',
    'job',
]

class BuildingController:
    @staticmethod
    def get_all_buildings():
        return Building.objects

    @staticmethod
    def find_by_id(building_id=None):
        building = Building.objects.get(pk=building_id)
        return building

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return Building.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_building(building_data=None):
        building = None
        message = '"name" and "job" fields are required'
        valid_data = ControllerHelpers.checkForAllUpdates(building_create_fields, building_data)

        if valid_data:
            building_name = building_data['name'].strip()
            job = building_data.get('job')
            mod_id = building_data.get('mod_id')
            existing_building = Building.objects(name__iexact=building_name)
            if existing_building:
                message = 'a building with that name and job "{}", "{}" already exists.'.format(building_name, job)
            else:
                building = Building(
                    name=building_name,
                    job=job,
                    created_by=mod_id
                )
                building = building.save()
                message = 'successfully created building'
        return {
            'value': building,
            'success': True if building else False,
            'message': message
        }

    @staticmethod
    def update_building(building_id=None, updates=None):
        building = None
        message = 'can not update buidling with empty request body'
        success = False
        has_updates = ControllerHelpers.checkForAnyUpdates(building_update_fields, updates)
        if building_id != None and has_updates != None:
            mod_id = updates.get('mod_id')
            job = building.get('job')
            building_name = updates.get('name')
            if building_name or mod_id:
                building = BuildingController.find_by_id(building_id=building_id)
                if building != None:
                    message = 'building with id "{}" not found'
                else:
                    if building_name:
                        building.name = building_name.strip()
                    if job:
                        buidling.job = building_job.strip()
                    if mod_id:
                        building.modified_by = mod_id
                    building.save()
                    success = True
                    message = 'successfully updated building'
        return {
            'value': buidling,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_building(building_id=None):
        building = None
        success = False
        message = 'building with id "{}" not found'.format(building_id)
        if building_id != None:
            building = BuildingController.find_by_id(building_id=building_id)
            if building != None:
                building.delete()
                success = True
                message = 'successfully deleted building'
        return {
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_all_buildings():
        Building.drop_collection()
