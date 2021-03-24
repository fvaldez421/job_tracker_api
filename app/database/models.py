from .db import db

class TestEntity(db.Document):
  name = db.StringField()
  description = db.StringField()

