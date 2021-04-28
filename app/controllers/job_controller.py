from app.database.models import Job

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
        job_name = job_data.get('name', '').strip()
        job_address = job_data.get('address', '').strip()
        job_number = job_data.get('number', '').strip()
        mod_id = job_data.get('mod_id')

        if job_name and job_address and job_number:
            existing_job = Job.objects(name__iexact=job_name)
            if existing_job:
                message = 'a job with the name "{}" already exists'.format(job_name)
            else:
                job = Job(
                    name=job_name,
                    address=job_address,
                    number=job_number,
                    created_by=mod_id
                )
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
        message = '"name", "address", or "number" field required'
        success = False
        if job_id != None or updates != None:
            mod_id = updates.get('mod_id')
            job_name = updates.get('name', '').strip()
            job_address = updates.get('address', '').strip()
            job_number = updates.get('number', '').strip()
            if job_name or job_address or job_number:
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


