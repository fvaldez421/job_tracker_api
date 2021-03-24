from flask import Blueprint, request
from ..database.models import TestEntity


jobs_bp = Blueprint('jobs', __name__)


@jobs_bp.route('/jobs', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return {
            "test_entities": TestEntity.objects
        }
    if request.method == 'POST':
        test_entity = TestEntity(name='my first test', description='some description here')
        test_entity.save()
        print(test_entity)
        return {
            "data": {
                "something": "here",
                "entity": test_entity
            }
        }