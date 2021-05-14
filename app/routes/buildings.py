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
        building = BuildingController.create_building(req_body)
        return {
            "building": building,
            "success": building != None
        }

    if request.method == 'DELETE':
        success = BuildingController.delete_all_buildings()
        return {
            "success": success
        }


@buildings_bp.route('/buildings/<building_id>', methods=['GET', 'PUT', 'DELETE'])
def building_by_id(building_id=None):
    if request.method == 'GET':
        return {
            "buildings": Building.objects(pk=building_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        building = BuildingController.update_building(building_id, req_body)
        return {
            "building": building,
            "success": building != None
        }
    if request.method == 'DELETE':
        building = BuildingController.delete_building(building_id)
        return {
            "building": building,
            "success": building != None
        }
