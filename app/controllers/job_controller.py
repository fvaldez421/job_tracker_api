from app.database.models import Job
from app.database.models import User



class JobController:
    @staticmethod
    def get_all_jobs():
        return Job.objects

    @staticmethod
    def get_single_job(job_id=None):
        job = Job.objects.get(pk=job_id)
        return job

    @staticmethod
    def create_job(job_data = None,user_id = None):
        job = None
        if 'name' in job_data and 'email' in job_data:
            job = Job(
                name = job_data['name'].strip(),
            )
            job = job.save()
        return job

    @staticmethod
    def update_job(job_id = None, updates = None):
        job = None
        success = False
        if job_id != None or updates != None:
            job = JobController.get_single_user(job_id=job_id)
            if job != None:
                if 'name' in updates: job.name = updates['name'].strip()
                if 'email' in updates: job.email = updates['email'].strip()
                job.save()
                success = True
        return success

    @staticmethod
    def delete_job(job_id = None):
        job = None
        success = False
        if job_id != None:
            job = JobController.get_single_job(job_id=job_id)
            if job != None:
                job.delete()
                success = True
        return success

    @staticmethod
    def delete_all_jobs():
        Job.drop_collection()