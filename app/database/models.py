import datetime
from .db import db


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


class User(DocumentWithDate):
    name = db.StringField()
    email = db.EmailField()


class Vendor(DocumentWithDateUser):
    name = db.StringField()


class Job(DocumentWithDateUser):
    name = db.StringField()
    address = db.StringField()
    number = db.IntField()
    #contract_amount = db.FloatField()
