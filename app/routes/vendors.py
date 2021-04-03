rom flask import Blueprint, request

from app.database.models import Vendor
from app.controllers.vendor_controller import VendorController

vendors_bp = Blueprint('vendors', __vendor__)


@vendors_bp.route('/vendors', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return {
            "vendors": VendorController.get_all_vendors()
        }

    if request.method == 'POST':
        req_body = request.json
        vendor = VendorrController.create_vendor(req_body)
        return {
            "vendor": vendor,
            "success": vendor != None
        }

    if request.method == 'DELETE':
        success = VendorController.delete_all_vendors()
        return {
            "success": success
        }


@vendors_bp.route('/vendors/<vendor_id>', methods=['GET', 'PUT', 'DELETE'])
def vendor_by_id(vendor_id=None):
    if request.method == 'GET':
        return {
            "vendors": Vendor.objects(pk=vendor_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        vendor = VendorController.update_vendor(vendor_id, req_body)
        return {
            "vendor": vendor,
            "success": vendor != None
        }
    if request.method == 'DELETE':
        vendor = VendorController.delete_vendor(vendor_id)
        return {
            "vendor": vendor,
            "success": vendor != None
        }
