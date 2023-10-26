from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class HabitEntry(db.Model, SerializerMixin):
    __tablename__ = "habit_entries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"))

    serialize_rules = ("-users.habit_entries", "-habits.habit_entries",)

    def __repr__(self):
        return f"<HabitEntry {self.id}>"

class Habit(db.Model, SerializerMixin):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.Integer)
    daily = db.Column(db.Boolean)
    weekly = db.Column(db.Boolean)
    monthly = db.Column(db.Boolean)
    yearly = db.Column(db.Boolean)

    users = db.relationship(
        'User', secondary="habit_entries", back_populates='habits')

    # habit_entries = db.relationship(
    #     "HabitEntry", backref="habit", cascade="all, delete")

    serialize_rules = ("-habit_entries.habits", "-users.habits",)

    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) > 0:
            return name
        raise ValueError("Error, must have name greater than zero.")

    def __repr__(self):
        return f"<Habit {self.name}>"

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)

    habits = db.relationship(
        'Habit', secondary="habit_entries", back_populates='users')

    # habit_entries = db.relationship(
    #     "HabitEntry", backref="user", cascade="all, delete")

    serialize_rules = ("-habit_entries.users","habits.users",)


    @validates("username")
    def validate_name(self, key, username):
        if username and len(username) > 0:
            return username
        raise ValueError("Error, must have username greater than zero.")

    def __repr__(self):
        return f"<User {self.username}>"

class EntryDate(db.Model, SerializerMixin):
    __tablename__ = "entry_dates"

    id = db.Column(db.Integer, primary_key=True)
    entry_performed_date = db.Column(db.String)
    entry_id = db.Column(db.Integer, db.ForeignKey("habit_entries.id"))

    habit_entries = db.relationship(
        "HabitEntry", backref="entry_date", cascade="all, delete")

    serialize_rules = ("-habit_entries.entry_date",)

    @validates("entry_performed_date")
    def validate_date(self, key, date):
        if date and len(date) > 0:
            return date
        raise ValueError("Error, must have date greater than zero.")

    def __repr__(self):
        return f"<EntryDate {self.entry_performed_date}>"