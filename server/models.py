from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class DailyHabit(db.Model, SerializerMixin):
    __tablename__ = "daily_habits"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # table relationships
    entries = db.relationship("entries", backref="daily_habit", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.daily_habit")

    # validation rules
    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) > 0:
            return name
        raise ValueError("Error, must have name greater than zero.")

class WeeklyHabit(db.Model, SerializerMixin):
    __tablename__ = "weekly_habits"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # table relationships
    entries = db.relationship("entries", backref="weekly_habit", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.weekly_habit")

    # validation rules
    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) > 0:
            return name
        raise ValueError("Error, must have name greater than zero.")

class MonthlyHabit(db.Model, SerializerMixin):
    __tablename__ = "monthly_habits"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # table relationships
    entries = db.relationship("entries", backref="monthly_habit", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.monthly_habit")

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
    name = db.Column(db.String)

    # table relationships
    entries = db.relationship("entries", backref="user", cascade="all, delete")

    # serilaize rules
    serialize_rules = ("-entries.user")

    # validation rules
    @validates("name")
    def validate_name(self, key, name):
        if name and len(name) > 0:
            return name
        raise ValueError("Error, must have name greater than zero.")

class Entry(db.Model, SerializerMix):
    __tablename__ = "entries"

    # table columns
    id = db.Column(db.Integer, primary_key=True)

    # table relationships/columns
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    dailyHabit_id = db.Column(db.Integer, db.ForeignKey("dailyHabit.id"))
    weeklyHabit_id = db.Column(db.Integer, db.ForeignKey("weeklyHabit.id"))
    monthlyHabit_id = db.Column(db.Integer, db.ForeignKey("monthlyHabit.id"))

    # serilaize rules
    serialize_rules = ("-daily_habit.entries, -weekly_habit.entries, -monthly_habit.entries, -user.entries")

    # validation rules