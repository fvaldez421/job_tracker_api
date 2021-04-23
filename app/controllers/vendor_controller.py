from app.database.models import Vendor
from app.database.models import User


class VendorController:
    @staticmethod
    def get_all_vendors():
        return Vendor.objects

    @staticmethod
    def find_by_id(vendor_id=None):
        vendor = Vendor.objects.get(pk=vendor_id)
        return vendor

    @staticmethod
    def find_by_name(query_name):
        return Vendor.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_vendor(vendor_data=None, user_id=None):
        vendor = None
        if 'name' in vendor_data:
            vendor_name = vendor_data['name'].strip()
            existing_vendor = Vendor.objects(name__iexact=vendor_name)
            if not existing_vendor:
                vendor = Vendor(name=vendor_name)
                vendor = vendor.save() 
        return vendor
        
    @staticmethod
    def update_vendor(vendor_id=None, updates=None):
        vendor = None
        success = False
        if vendor_id != None or updates != None:
            vendor = VendorController.find_by_id(vendor_id=vendor_id)
            if vendor != None:
                if 'name' in updates:
                    vendor.name = updates['name'].strip()
                    vendor.save()
                    success = True
        return vendor if success else None

    @staticmethod
    def delete_vendor(vendor_id=None):
        vendor = None
        success = False
        if vendor_id != None:
            vendor = VendorController.find_by_id(vendor_id=vendor_id)
            if vendor != None:
                vendor.delete()
                success = True
        return success

    @staticmethod
    def delete_all_vendors():
        Vendor.drop_collection()
