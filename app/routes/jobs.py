from flask import Blueprint, request

from app.database.models import Job
from app.controllers.job_controller import JobController

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        text_query = request.args.get('q', None)
        jobs = None
        if text_query != None:
            jobs = JobController.find_by_name(text_query)
        else:
            jobs = JobController.get_all_jobs()
        return {
            "jobs": jobs
        }

    if request.method == 'POST':
        req_body = request.json
        job = JobController.create_job(req_body)
        return {
            "job": job,
            "success": job != None
        }

    if request.method == 'DELETE':
        success = JobController.delete_all_jobs()
        return {
            "success": success
        }


@jobs_bp.route('/jobs/<job_id>', methods=['GET', 'PUT', 'DELETE'])
def job_by_id(job_id=None):
    if request.method == 'GET':
        return {
            "jobs": Job.objects(pk=job_id)
        }
    if request.method == 'PUT':
        req_body = request.json
        job = JobController.update_vendor(job_id, req_body)
        return {
            "job": job,
            "success": job != None
        }
    if request.method == 'DELETE':
        job = JobController.delete_job(job_id)
        return {
            "job": job,
            "success": job != None
        }
