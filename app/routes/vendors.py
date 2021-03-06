from flask import Blueprint, request

from app.database.models import Vendor
from app.controllers.vendor_controller import VendorController

vendors_bp = Blueprint('vendors', __name__)


@vendors_bp.route('/vendors', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        vendors = None
        if text_query != None:
            vendors = VendorController.find_by_name(text_query)
        else:
            vendors = VendorController.get_all_vendors()
        return {
            "vendors": vendors
        }

    if request.method == 'POST':
        req_body = request.json
        vendor = VendorController.create_vendor(req_body)
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
