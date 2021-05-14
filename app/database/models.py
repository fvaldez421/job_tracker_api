import datetime
from enum import Enum

from .db import db


# enums
class JobStatus(Enum):
    DRAFT = 'draft'
    IN_PROGRESS = 'in_progress'
    ARCHIVED = 'archived'


class MaterialType(Enum):
    LUMBER = 'lumber'
    CONCRETE = 'concrete'
    SIDING = 'siding'
    REBAR = 'rebar'


# utility models
class DocumentWithDate(db.Document):
    meta = {"allow_inheritance": True}
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def set_date(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.set_date(self, *args, **kwargs)
        return super(db.Document, self).save(*args, **kwargs)


class DocumentWithUser(db.Document):
    meta = {"allow_inheritance": True}
    created_by = db.StringField()
    modified_by = db.StringField()

    def set_user(self, *args, **kwargs):
        created_by = None
        modified_by = None
        if hasattr(self, 'created_by'):
            created_by = self.created_by
        if hasattr(self, 'modified_by'):
            modified_by = self.modified_by
        if created_by != None or modified_by != None:
            if not self.created_by and created_by:
                self.created_by = created_by
            self.modified_by = created_by if modified_by == None else modified_by

    def save(self, *args, **kwargs):
        self.set_user(self, *args, **kwargs)
        return super(db.Document, self).save(*args, **kwargs)


class DocumentWithDateUser(DocumentWithDate, DocumentWithUser):
    def save(self, *args, **kwargs):
        if hasattr(self, 'set_date'):
            self.set_date(self, *args, **kwargs)
        if hasattr(self, 'set_user'):
            self.set_user(self, *args, **kwargs)
        return super(db.Document, self).save(*args, **kwargs)


# models
class User(DocumentWithDate):
    name = db.StringField()
    email = db.EmailField()


class Building(DocumentWithDateUser):
    name = db.StringField()
    number = db.IntField()
    progress = db.IntField(default=0)
    calendar = db.StringField()


class Delivery(DocumentWithDateUser):
    date = db.DateTimeField()
    job = db.StringField()
    vendor = db.StringField()
    _material_type = db.StringField(required=True)
    @property
    def material_type(self):
        return self._material_type
    @material_type.setter
    def material_type(self, next_material):
        if next_material == MaterialType.LUMBER.value \
            or next_material == MaterialType.CONCRETE.value \
                or next_material == MaterialType.SIDING.value \
                    or next_material == MaterialType.REBAR.value:
            self._material_type = next_material

class Vendor(DocumentWithDateUser):
    name = db.StringField()

class GeneralContractor(DocumentWithDateUser):
    name = db.StringField()

# keep aligned with Job update fields (helpers/job_helpers)
class Job(DocumentWithDateUser):
    name = db.StringField()
    address = db.StringField()
    number = db.IntField()
    gen_con = db.StringField()
    progress = db.IntField(default=0)
    description = db.StringField()
    notes = db.StringField()
    _status = db.StringField(default=JobStatus.DRAFT.value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, next_status):
        if next_status == JobStatus.DRAFT.value \
            or next_status == JobStatus.IN_PROGRESS.value \
                or next_status == JobStatus.ARCHIVED.value:
            self._status = next_status
