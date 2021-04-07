from app.database.models import Vendor


class VendorController:
    @staticmethod
    def get_all_vendors():
        return Vendor.objects

    @staticmethod
    def get_single_vendor(vendor_id=None):
        vendor = Vendor.objects.get(pk=vendor_id)
        print(vendor)
        return vendor

    @staticmethod
    def create_vendor(vendor_data = None):
        vendor = None
        if 'name' in vendor_data:
            existing_vendor = Vendor.objects(name=vendor_data['name'])
            if not existing_vendor:
                vendor = Vendor(
                    name = vendor_data['name'],
                )
                vendor = vendor.save()
        return vendor

    @staticmethod
    def update_vendor(vendor_id = None, updates = None):
        vendor = None
        success = False
        print(vendor_id, updates)
        if vendor_id != None or updates != None:
            vendor = VendorController.get_single_vendor(vendor_id=vendor_id)
            if vendor != None:
                if 'name' in updates: vendor.name = updates['name']
                vendor.save()
                success = True
        return success

    @staticmethod
    def delete_vendor(vendor_id = None):
        vendor = None
        success = False
        print(vendor_id)
        if vendor_id != None:
            vendor = VendorController.get_single_vendor(vendor_id=vendor_id)
            if vendor != None:
                vendor.delete()
                success = True
        return success

    @staticmethod
    def delete_all_vendors():
        Vendor.drop_collection()