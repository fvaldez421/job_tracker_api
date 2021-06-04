from app.database.models import Vendor
from app.helpers.controller_helpers import ControllerHelpers
from app.helpers.date_helpers import DateHelpers

vendor_create_fields = [
    'name'
]
vendor_update_fields = [
    'name'
]

class VendorController:
    @staticmethod
    def get_all_vendors():
        return Vendor.objects

    @staticmethod
    def find_by_id(vendor_id=None):
        vendors = Vendor.objects(pk=vendor_id)
        if len(vendors) > 0:
            return vendors[0]
        return None

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return Vendor.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_vendor(vendor_data=None):
        vendor = None
        message = '"name" and "job" fields are required'
        valid_data = ControllerHelpers.checkForAllUpdates(vendor_create_fields, vendor_data)

        if valid_data:
            vendor_name = vendor_data['name'].strip()
            mod_id = vendor_data.get('mod_id')
            existing_vendor = Vendor.objects(name__iexact=vendor_name)
            if existing_vendor:
                message = 'a vendor with that name and job "{}", "{}" already exists.'.format(vendor_name, job)
            else:
                vendor = Vendor(
                    name=vendor_name,
                    created_by=mod_id
                )
                vendor = vendor.save()
                message = 'successfully created vendor'
        return {
            'value': vendor,
            'success': True if vendor else False,
            'message': message
        }

    @staticmethod
    def update_vendor(vendor_id=None, updates=None):
        vendor = None
        message = 'can not update vendor with empty request body'
        success = False
        has_updates = ControllerHelpers.checkForAnyUpdates(vendor_update_fields, updates)
        if vendor_id != None and has_updates != None:
            mod_id = updates.get('mod_id')
            vendor_name = updates.get('name')
            vendor = VendorController.find_by_id(vendor_id=vendor_id)
            if vendor == None:
                message = 'vendor with id "{}" not found'
            else:
                if vendor_name:
                    vendor.name = vendor_name.strip()
                if mod_id:
                    vendor.modified_by = mod_id
                
                vendor.save()
                success = True
                message = 'successfully updated vendor'
        return {
            'value': vendor,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_vendor(vendor_id=None):
        vendor = None
        success = False
        message = 'vendor with id "{}" not found'.format(vendor_id)
        if vendor_id != None:
            vendor = VendorController.find_by_id(vendor_id=vendor_id)
            if vendor != None:
                vendor.delete()
                success = True
                message = 'successfully deleted vendor'
        return {
            'success': success,
            'message': message
        }
    

    @staticmethod
    def delete_all_vendors():
        Vendor.drop_collection()
