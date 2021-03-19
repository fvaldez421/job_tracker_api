from flask import Blueprint, request

jobs_bp = Blueprint('jobs', __name__)


@jobs_bp.route('/jobs', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "This is an example for a jobs route"
    if request.method == 'POST':
        return {
            "data": {
                "something": "here"
            }
        }
        