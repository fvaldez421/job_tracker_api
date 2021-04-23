from flask import Blueprint, request

from app.database.models import Job
from app.controllers.job_controller import JobController

jobs_bp = Blueprint('jobs', __name__)


@jobs_bp.route('/jobs', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return {
            "test_entities": []
        }
    if request.method == 'POST':
        print(request.json)
        return {
            "data": {
                "something": "here",
                "entity": {}
            }
        }
