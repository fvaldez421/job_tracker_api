from flask import Blueprint, request

from app.database.models import Building
from app.controllers.building_controller import BuildingController

buildings_bp = Blueprint('buildings', __name__)


@buildings_bp.route('/buildings', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        buildings = None
        if text_query != None:
            buildings = BuildingController.find_by_name(text_query)
        else:
            buildings = BuildingController.get_all_buildings()
        return {
            "buildings": buildings
        }

    if request.method == 'POST':
        req_body = request.json
        res = BuildingController.create_building(req_body)
        return {
            'building': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }

    if request.method == 'DELETE':
        success = BuildingController.delete_all_buildings()
        return {
            "success": success
        }


@buildings_bp.route('/buildings/<building_id>', methods=['GET', 'PUT', 'DELETE'])
def building_by_id(building_id=None):
    if request.method == 'GET':
        message = 'building not found'
        building = BuildingController.find_by_id(building_id)
        return {
            'building': building,
            'success': True if building else False,
            'message': None if building else message
        }
    if request.method == 'PUT':
        req_body = request.json
        res = BuildingController.update_building(building_id, req_body)
        return {
            'building': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }
    if request.method == 'DELETE':
        res = BuildingController.delete_building(building_id)
        return {
            'success': res.get('success', False),
            'message': res.get('message')
        }

