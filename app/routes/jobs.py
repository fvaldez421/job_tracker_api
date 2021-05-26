from flask import Blueprint, request
from flask_cors import cross_origin

from app.controllers.job_controller import JobController

jobs_bp = Blueprint('jobs', __name__)


@jobs_bp.route('/jobs', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        jobs = None
        if text_query != None:
            jobs = JobController.find_by_name(text_query)
        else:
            jobs = JobController.get_all_jobs()
        return {
            'jobs': jobs
        }

    if request.method == 'POST':
        req_body = request.json
        res = JobController.create_job(req_body)
        return {
            'job': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }

    # should protect with basic auth
    if request.method == 'DELETE':
        success = JobController.delete_all_jobs()
        # hard coded -- not for use on prod
        return {
            'success': True
        }


@jobs_bp.route('/jobs/<job_id>', methods=['GET', 'PUT', 'DELETE'])
def job_by_id(job_id=None):
    if request.method == 'GET':
        message = 'job not found'
        job = JobController.find_by_id(job_by_id)
        return {
            'job': job,
            'success': True if job else False,
            'message': None if job else message
        }
    if request.method == 'PUT':
        req_body = request.json
        res = JobController.update_job(job_id, req_body)
        return {
            'job': res.get('value'),
            'success': res.get('success', False),
            'message': res.get('message')
        }
    if request.method == 'DELETE':
        res = JobController.delete_job(job_id)
        return {
            'success': res.get('success', False),
            'message': res.get('message')
        }
