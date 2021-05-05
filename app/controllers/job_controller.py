from app.database.models import Job, JobStatus
from app.helpers.controller_helpers import ControllerHelpers

# keep aligned with Job db model (database/models)
job_create_fields = [
    'name',
    'address',
    'number'
]
job_update_fields = [
    'name',
    'address',
    'number',
    'gen_con',
    'progress',
    'description',
    'notes',
    'status'
]

class JobController:
    @staticmethod
    def get_all_jobs():
        return Job.objects

    @staticmethod
    def find_by_id(job_id=None):
        job = Job.objects.get(pk=job_id)
        return job

    @staticmethod
    def find_by_name(query_name, specialValue=None):
        return Job.objects(name__icontains=query_name.strip())

    @staticmethod
    def create_job(job_data=None):
        job = None
        message = '"name", "address", and "number" fields are all required'
        valid_data = ControllerHelpers.checkForAllUpdates(job_create_fields, job_data)

        if valid_data:
            job_name = job_data.get('name', '').strip()
            job_address = job_data.get('address', '').strip()
            job_number = job_data.get('number', '').strip()
            gen_con = job_data.get('gen_con', '')
            progress = job_data.get('progress', 0)
            status = job_data.get('status', JobStatus.DRAFT.value)
            desc = job_data.get('description', '').strip()
            notes = job_data.get('notes', '').strip()
            mod_id = job_data.get('mod_id')

            existing_job = Job.objects(name__iexact=job_name)
            if existing_job:
                message = 'a job with the name "{}" already exists'.format(job_name)
            else:
                job = Job(
                    name=job_name,
                    address=job_address,
                    gen_con=gen_con,
                    progress=progress,
                    description=desc,
                    notes=notes,
                    created_by=mod_id
                )
                if status:
                    job.status = status
                if job_number:
                    job.number = job_number
                job = job.save()
                message = 'successfully created job'
        return {
            'value': job,
            'success': True if job else False,
            'message': message
        }

    @staticmethod
    def update_job(job_id=None, updates=None):
        job = None
        message = 'can not update job with empty request body'
        success = False
        has_updates = ControllerHelpers.checkForAnyUpdates(job_update_fields, updates)
        if job_id != None and has_updates:
            mod_id = updates.get('mod_id')
            job_name = updates.get('name', '').strip()
            job_address = updates.get('address', '').strip()
            job_number = updates.get('number', '').strip()
            gen_con = updates.get('gen_con', '').strip()
            desc = updates.get('description', '').strip()
            notes = updates.get('notes', '').strip()
            progress = updates.get('progress')
            status = updates.get('status')

            job = JobController.find_by_id(job_id=job_id)
            if not Job:
                message = 'job with id "{}" not found'.format(job_id)
            else:
                if job_name:
                    job.name = job_name
                if job_address:
                    job.address = job_address
                if job_number:
                    job.number = job_number
                if gen_con:
                    job.gen_con = gen_con
                if progress:
                    job.progress = progress
                if status:
                    job.status = status
                if desc:
                    job.description = desc
                if notes:
                    job.notes = notes
                if mod_id:
                    job.modified_by = mod_id
                job.save()
                success = True
                message = 'successfully updated job'
        return {
            'value': job,
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_job(job_id=None):
        job = None
        success = False
        message = 'job with id "{}" not found'.format(job_id)
        if job_id != None:
            job = JobController.find_by_id(job_id=job_id)
            if job != None:
                job.delete()
                success = True
                message = 'successfully deleted job'
        return {
            'success': success,
            'message': message
        }

    @staticmethod
    def delete_all_jobs():
        Job.drop_collection()
