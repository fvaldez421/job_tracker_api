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
        if 'name' in job_data and 'address' in job_data and 'number' in job_data:
            job_name = job_data['name'].strip()
            job_address = job_data['address'].strip()
            job_number = job_data['number']
            mod_id = job_data.get('mod_id')
            existing_job = Job.objects(name__iexact=job_name)
            existing_address = Job.objects(address__iexact=job_address)
            if not existing_job:
                job = Job(
                    name=job_name,
                    address=job_address,
                    number=job_number,
                    created_by=mod_id
                )
                job = job.save()
        return job

    @staticmethod
    def update_job(job_id=None, updates=None):
        job = None
        success = False
        if job_id != None or updates != None:
            mod_id = updates.get('mod_id')
            job_name = updates.get('name')
            if job_name or mod_id:
                job = JobController.find_by_id(job_id=job_id)
                if job != None:
                    if job_name:
                        job.name = job_name.strip()
                    if mod_id:
                        job.modified_by = mod_id
                    job.save()
                    success = True
        return job if success else None

    @staticmethod
    def delete_job(job_id=None):
        job = None
        success = False
        if job_id != None:
            job = JobController.find_by_id(job_id=job_id)
            if job != None:
                job.delete()
                success = True
        return success

    @staticmethod
    def delete_all_jobs():
        Job.drop_collection()


