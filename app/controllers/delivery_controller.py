from app.database.models import Delivery, MaterialType
from app.helpers.controller_helpers import ControllerHelpers
from app.helpers.date_helpers import DateHelpers

# keep aligned with Delivery db model (database/models)
delivery_create_fields = [
    'date',
    'job',
    'vendor',
    'material_type'
]
delivery_update_fields = [
    'date',
    'job',
    'vendor',
    'material_type'
]

class DeliveryController:
    @staticmethod
    def get_all_deliveries():
        return Delivery.objects

    @staticmethod
    def find_by_id(delivery_id=None):
        deliveries = Delivery.objects(pk=delivery_id)
        if len(deliveries) > 0:
            return deliveries[0]
        return None

    @staticmethod
    def find_by_date(query_delivery, specialValue=None):
        return Delivery.objects(delivery__contains=query_delivery.strip())

    @staticmethod
    def create_delivery(delivery_data=None):
        delivery = None
        message = '"date", "job", and "vendor" fields are all required'
        valid_data = ControllerHelpers.checkForAllUpdates(delivery_create_fields, delivery_data)

        if valid_data:
            date = DateHelpers.convert_from_ms(delivery_data.get('date'))
            job = delivery_data.get('job', '').strip()
            vendor = delivery_data.get('vendor', '').strip()
            material_type = delivery_data.get('material_type', '').strip()
            mod_id = delivery_data.get('mod_id')
            existing_delivery = Delivery.objects(date=date, job=job, _material_type=material_type)
            if existing_delivery:
                message = 'a delivery with the date, job, and material type "{}", "{}", "{}" already exists'.format(date, job, material_type)
            else:
                delivery = Delivery(
                    date=date,
                    job=job,
                    vendor=vendor
                )
                if material_type:
                    delivery.material_type = material_type
                delivery = delivery.save()
                message = 'successfully created delivery'
        return {
            'value': delivery,
            'success': True if delivery else False,
            'message': message
        }

    @staticmethod
    def update_delivery(delivery_id=None, updates=None):
        delivery = None
        message = 'can not update delivery with empty request body'
        success = False
        has_updates = ControllerHelpers.checkForAnyUpdates(delivery_update_fields, updates)
        if delivery_id != None and has_updates:
            mod_id = updates.get('mod_id')
            date = DateHelpers.convert_from_ms(updates.get('date'))
            job = updates.get('job', '').strip()
            vendor = updates.get('vendor', '').strip()
            material_type = updates.get('material_type', '').strip()

            delivery = DeliveryController.find_by_id(delivery_id=delivery_id)
            if not Delivery:
                message = 'delivery with id "{}" not found'.format(delivery_id)
            else:
                if date:
                    delivery.date = date
                if job:
                    delivery.job = job
                if vendor:
                    delivery.vendor = vendor
                if material_type:
                    delivery.material_type = material_type
                if mod_id:
                    delivery.modified_by = mod_id
                delivery.save()
                success = True
                message = 'successfully updated delivery'
        return {
            'value': delivery,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_delivery(delivery_id=None):
        delivery = None
        success = False
        message = 'delivery with id "{}" not found'.format(delivery_id)
        if delivery_id != None:
            delivery = DeliveryController.find_by_id(delivery_id=delivery_id)
            if delivery != None:
                delivery.delete()
                success = True
                message = 'successfully deleted delivery'
        return {
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_all_deliveries():
        Delivery.drop_collection()
