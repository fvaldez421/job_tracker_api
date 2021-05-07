from flask import Blueprint, request

from app.database.models import GeneralContractor
from app.controllers.gencon_controller import GeneralContractorController

generalcontractors_bp = Blueprint('generalcontractors', __name__)


@generalcontractors_bp.route('/generalcontractors', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        generalcontractors = None
        if text_query != None:
            generalcontractors = GeneralContractorController.find_by_name(text_query)
        else:
            generalcontractors = GeneralContractorController.get_all_generalcontractors()
        return {
            "generalcontractors": generalcontractors
        }

    if request.method == 'POST':
        req_body = request.json
        generalcontractor = GeneralContractorController.create_generalcontractor(req_body)
        return {
            "generalcontractor": generalcontractor,
            "success": generalcontractor != None
        }

    if request.method == 'DELETE':
        success = GeneralContractorController.delete_all_generalcontractors()
        return {
            "success": success
        }


@generalcontractors_bp.route('/generalcontractors/<generalcontractor_id>', methods=['GET', 'PUT', 'DELETE'])
def generalcontractor_by_id(generalcontractor_id=None):
    if request.method == 'GET':
        return {
            "generalcontractors": GeneralContractor.objects(pk=generalcontractor_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        generalcontractor = GeneralContractorController.update_generalcontractor(generalcontractor_id, req_body)
        return {
            "generalcontractor": generalcontractor,
            "success": generalcontractor != None
        }
    if request.method == 'DELETE':
        generalcontractor = GeneralContractorController.delete_generalcontractor(generalcontractor_id)
        return {
            "generalcontractor": generalcontractor,
            "success": generalcontractor != None
        }
