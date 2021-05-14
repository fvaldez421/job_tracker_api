from flask import Blueprint, request

from app.database.models import Delivery
from app.controllers.delivery_controller import DeliveryController

deliveries_bp = Blueprint('deliveries', __name__)


@deliveries_bp.route('/deliveries', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        deliveries = None
        if text_query != None:
            deliveries = DeliveryController.find_by_name(text_query)
        else:
            deliveries = DeliveryController.get_all_deliveries()
        return {
            "deliveries": deliveries
        }

    if request.method == 'POST':
        req_body = request.json
        delivery = DeliveryController.create_delivery(req_body)
        return {
            "delivery": delivery,
            "success": delivery != None
        }

    if request.method == 'DELETE':
        success = DeliveryController.delete_all_deliveries()
        return {
            "success": success
        }


@deliveries_bp.route('/deliveries/<delivery_id>', methods=['GET', 'PUT', 'DELETE'])
def delivery_by_id(delivery_id=None):
    if request.method == 'GET':
        return {
            "deliveries": Delivery.objects(pk=delivery_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        delivery = DeliveryController.update_delivery(delivery_id, req_body)
        return {
            "delivery": delivery,
            "success": delivery != None
        }
    if request.method == 'DELETE':
        delivery = DeliveryController.delete_delivery(delivery_id)
        return {
            "delivery": delivery,
            "success": delivery != None
        }
