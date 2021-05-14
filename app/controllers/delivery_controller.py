from app.database.models import Delivery


class DeliveryController:
    @staticmethod
    def get_all_deliveries():
        return Delivery.objects

    @staticmethod
    def find_by_id(delivery_id=None):
        delivery = Delivery.objects.get(pk=delivery_id)
        return delivery

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return Delivery.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_delivery(delivery_data=None):
        delivery = None
        if 'date' in delivery_data and 'job' in delivery_data and \
            'vendor' in delivery_data and 'material_type' in delivery_data:
            mod_id = delivery_data.get('mod_id')
            delivery_date = delivery_data['date'].strip()
            job = delivery_data.get('job')
            vendor = delivery_data.get('vendor')
            material_type = delivery_data.get('material_type')
            existing_delivery = Delivery.objects(date__exact=delivery_date, job__exact=job, _material_type__exact=material_type)
            if not existing_delivery:
                delivery = Delivery(
                    date=delivery_date,
                    job=job,
                    vendor=vendor,
                    material_type=material_type,
                    created_by=mod_id
                )
                delivery = delivery.save()
        return delivery

    @staticmethod
    def update_delivery(delivery_id=None, updates=None):
        delivery = None
        success = False
        if delivery_id != None or updates != None:
            mod_id = updates.get('mod_id')
            delivery_name = updates.get('name')
            if delivery_name or mod_id:
                delivery = DeliveryController.find_by_id(delivery_id=delivery_id)
                if delivery != None:
                    if delivery_name:
                        delivery.name = delivery_name.strip()
                    if mod_id:
                        delivery.modified_by = mod_id
                    delivery.save()
                    success = True
        return delivery if success else None

    @staticmethod
    def delete_delivery(delivery_id=None):
        delivery = None
        success = False
        if delivery_id != None:
            delivery = DeliveryController.find_by_id(delivery_id=delivery_id)
            if delivery != None:
                delivery.delete()
                success = True
        return success

    @staticmethod
    def delete_all_deliverys():
        Delivery.drop_collection()
