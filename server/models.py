from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

# Association table to store many-to-many relationship between users and habits
class HabitEntry(db.Model, SerializerMixin):
    __tablename__ = "habit_entries"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"))

    # serilaize rules
    serialize_rules = ("-user.habit_entries", "-habit.habit_entries",)

    # validation rules
class Habit(db.Model, SerializerMixin):
    __tablename__ = "habits"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.Integer)
    daily = db.Column(db.Boolean)
    weekly = db.Column(db.Boolean)
    monthly = db.Column(db.Boolean)
    yearly = db.Column(db.Boolean)

    # Relationship mapping the habit to related users
    users = db.relationship(
        'User', secondary="habit_entries", backref='habit')

    # Relationship mapping the habit to related habit_entries
    habit_entries = db.relationship(
        "HabitEntry", backref="habit", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-habit_entries.habit",)

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
    age = db.Column(db.Integer)

    # Relationship mapping the user to related habits
    habits = db.relationship(
        'Habit', secondary="habit_entries", backref='user')

    # Relationship mapping the user to related habit_entries
    habit_entries = db.relationship(
        "HabitEntry", backref="user", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-habit_entries.user",)

    # validation rules
    @validates("username")
    def validate_name(self, key, username):
        if username and len(username) > 0:
            return username
        raise ValueError("Error, must have username greater than zero.")

class EntryDate(db.Model, SerializerMixin):
    __tablename__ = "entry_dates"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    entry_performed_date = db.Column(db.String)
    entry_id = db.Column(db.Integer, db.ForeignKey("habit_entries.id"))

    # Relationship mapping the user to related habit_entries
    habit_entries = db.relationship(
        "HabitEntry", backref="entry_date", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-habit_entries.entry_date",)

    # validation rules
    @validates("entry_performed_date")
    def validate_date(self, key, date):
        if date and len(date) > 0:
            return date
        raise ValueError("Error, must have date greater than zero.")