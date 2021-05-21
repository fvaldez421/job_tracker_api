from app.database.models import Building


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
        if 'name' in building_data and 'job' in building_data:
            building_name = building_data['name'].strip()
            job = building_data.get('job')
            mod_id = building_data.get('mod_id')
            existing_building = Building.objects(name__iexact=building_name)
            if not existing_building:
                building = Building(
                    name=building_name,
                    created_by=mod_id
                )
                building = building.save()
        return building

    @staticmethod
    def update_building(building_id=None, updates=None):
        building = None
        success = False
        if building_id != None or updates != None:
            mod_id = updates.get('mod_id')
            job = building.get('job')
            building_name = updates.get('name')
            if building_name or mod_id:
                building = BuildingController.find_by_id(building_id=building_id)
                if building != None:
                    if building_name:
                        building.name = building_name.strip()
                    if mod_id:
                        building.modified_by = mod_id
                    building.save()
                    success = True
        return building if success else None

    @staticmethod
    def delete_building(building_id=None):
        building = None
        success = False
        if building_id != None:
            building = BuildingController.find_by_id(building_id=building_id)
            if building != None:
                building.delete()
                success = True
        return success

    @staticmethod
    def delete_all_buildings():
        Building.drop_collection()
