#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, abort, session, jsonify

from flask_restful import Resource

# Local imports
from config import app, db, api

# Add Models here
from model import User, Entry, DailyHabit, WeeklyHabit, MonthlyHabit

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class DailyHabits(Resource):
    def get(self):
        daily_habits = [habits.to_dict() for habits in DailyHabit.query.all()]
        return make_response(daily_habits, 200)

    def post(self):
        try:
            habit = {
                name = request.json["name"],
            }
            db.session.add(habit)
            db.session.commit()
            return make_response(habit.to_dict(), 201)
        except:
            return make_response({"Error": "post failed"}, 400)

api.add_resource(DailyHabit, "/daily_habit")

class DailyHabitsById(Resource):
    def get(self, id):
        try:
            habit = DailyHabit.query.filter_by(id = id).first()
            return make_response(daily_habits.to_dict(), 200)
        except:
            return make_response({"error": ["habit not found"]}, 404)

    def delete(self, id):
        habit = DailyHabit.query.filter_by(id = id).first()
        if not habit:
            return make_response({"error": ["habit not found"]}, 404)
        db.session.delete(habit)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        try:
            habit = DailyHabit.query.filter_by(id = id).first()
            request_json = request.get_json()

            for key in request_json:
                setattr(self, key, request_json[key])

            db.session.add(habit)
            db.session.commit()

            return make_response(habit.to_dict(), 202)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(DailyHabitsById, "/daily_habit/<int:id>")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)

    def post(self):
        try:
            user = {
                name = request.json["name"]
            }
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 201)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(User, "/users")

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"error": ["user not found"]}, 404)
        return make_response(user.to_dict, 200)

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"error": ["user not found"]}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"error": ["user not found"]}, 404)
        try:
            for attr in request.json: 
                setattr(user, attr, request.json[attr])
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 202)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(UsersById, "/users/<int:id>")

class HabitEntries(Resource):
    def get(self):
        entry = [entry.to_dict() for entry in HabitEntry.query.all()]
        return make_response(entry, 200)

    def post(self):
        try:
            entry = {
                name = request.json["name"]
            }
            db.session.add(entry)
            db.session.commit()
            return make_response(entry.to_dict(), 201)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(HabitEntries, "/habit_entries")

class HabitEntriesById(Resource):
    def get(self, id):
        entry = HabitEntry.query.filter_by(id = id).first()
        if not entry:
            return make_response({"error": ["entry not found"]}, 404)
        return make_response(entry.to_dict(), 200)

    def delete(self, id):
        entry = HabitEntry.query.filter_by(id = id).first()
        if not entry:
            return make_response({"error": ["entry not found"]}, 404)
        db.session.delete(entry)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        entry = HabitEntry.query.filter(HabitEntry.id == id).first()
        if not entry:
            return make_response({"error": ["entry not found"]}, 404)
        try:
            for attr in request.json: 
                setattr(entry, attr, request.json[attr])
            db.session.add(entry)
            db.session.commit()
            return make_response(entry.to_dict(), 202)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(HabitEntries, "/habit_entries/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
