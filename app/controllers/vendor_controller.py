from app.database.models import Vendor


class VendorController:
    @staticmethod
    def get_all_vendors():
        return Vendor.objects

    @staticmethod
    def find_by_id(vendor_id=None):
        vendor = Vendor.objects.get(pk=vendor_id)
        return vendor

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return Vendor.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_vendor(vendor_data=None):
        vendor = None
        if 'name' in vendor_data:
            vendor_name = vendor_data['name'].strip()
            mod_id = vendor_data.get('mod_id')
            existing_vendor = Vendor.objects(name__iexact=vendor_name)
            if not existing_vendor:
                vendor = Vendor(
                    name=vendor_name,
                    created_by=mod_id
                )
                vendor = vendor.save()
        return vendor

    @staticmethod
    def update_vendor(vendor_id=None, updates=None):
        vendor = None
        success = False
        if vendor_id != None or updates != None:
            mod_id = updates.get('mod_id')
            vendor_name = updates.get('name')
            if vendor_name or mod_id:
                vendor = VendorController.find_by_id(vendor_id=vendor_id)
                if vendor != None:
                    if vendor_name:
                        vendor.name = vendor_name.strip()
                    if mod_id:
                        vendor.modified_by = mod_id
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
