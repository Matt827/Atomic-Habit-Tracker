from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

# Association table to store many-to-many relationship between users and habits
class Entry(db.Model, SerializerMixin):
    __tablename__ = "entries"

    # table columns
    id = db.Column(db.Integer, primary_key=True)

    # table relationships/columns
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"))

    # serilaize rules
    serialize_rules = ("-user.entries", )

    # validation rules
class Habit(db.Model, SerializerMixin):
    __tablename__ = "habits"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # table relationships
    entries = db.relationship(
        "Entry", backref="habit", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.habit", )

    # validation rules
    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) > 0:
            return name
        raise ValueError("Error, must have name greater than zero.")

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

    # table relationships
    entries = db.relationship("Entry", backref="user", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.user", )

    # validation rules
    @validates("username")
    def validate_name(self, key, username):
        if username and len(username) > 0:
            return username
        raise ValueError("Error, must have username greater than zero.")

