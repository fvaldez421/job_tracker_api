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
        if 'name' in delivery_data:
            delivery_name = delivery_data['name'].strip()
            mod_id = delivery_data.get('mod_id')
            existing_delivery = Delivery.objects(name__iexact=delivery_name)
            if not existing_delivery:
                delivery = Delivery(
                    name=delivery_name,
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
