import datetime
from .db import db


class User(db.Document):
    name = db.StringField()
    email = db.EmailField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)
    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

class Vendor(db.Document)
    vendor = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)
    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Vendor, self).save(*args, **kwargs)