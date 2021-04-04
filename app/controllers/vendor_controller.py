from app.database.models import Vendor


class VendorController:
    @staticmethod
    def get_all_vendors():
        return Vendors.objects

    @staticmethod
    def get_single_vendor(vendor_id=None):
        vendor = Vendor.objects.get(pk=vendor_id)
        print(vendor)
        return vendor

    @staticmethod
    def create_vendor(vendor_data = None):
        vendor = None
        if 'vendor' in vendor_data:
            vendor = Vendor(
                vendor = vendor_data['vendor'],
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
                if 'vendor' in updates: vendor.name = updates['vendor']
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
        User.drop_collection()