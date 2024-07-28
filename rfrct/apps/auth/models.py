from extensions import db
from flask_security import UserMixin, RoleMixin
from mongoengine.fields import (
    BinaryField,
    BooleanField,
    DateTimeField,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)


class Role(db.Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)
    permissions = ListField(required=False)

class User(db.Document, UserMixin):
    email = db.StringField(max_length=255, unique=True)
    username = db.StringField(max_length=255, unique=True)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    fs_uniquifier = StringField(max_length=64, unique=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role), default=[])

