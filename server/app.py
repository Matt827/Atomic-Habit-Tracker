#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response, abort, session, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api, bcrypt

# Add Models here
from models import HabitEntry, EntryDate, User, Habit

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Habits(Resource):
    def get(self):
        habits = [habit.to_dict(rules=("-habit_entries",)) for habit in Habit.query.all()]
        return make_response(habits, 200)

    def post(self):
        try:
            habit = Habit(
                name = request.json["name"],
                duration = request.json["duration"],
                daily = request.json["daily"],
                weekly = request.json["weekly"],
                monthly = request.json["monthly"],
                yearly = request.json["yearly"]
            )
            db.session.add(habit)
            db.session.commit()
            return make_response(habit.to_dict(), 201)
        except:
            return make_response({"Error": "post failed"}, 400)

api.add_resource(Habits, "/habits")

class HabitsById(Resource):
    def get(self, id):
        habit = Habit.query.filter_by(id = id).first()
        if not habit: 
            return make_response({"error": ["habit not found"]}, 404)
        return make_response(habit.to_dict(rules = ("-habit_entries",)), 200)

    def delete(self, id):
        habit = Habit.query.filter_by(id = id).first()
        if not habit:
            return make_response({"error": ["habit not found"]}, 404)
        db.session.delete(habit)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        habit = Habit.query.filter_by(id = id).first()
        if not habit:
            return make_response({"error": ["habit not found"]}, 404)
        try:
            for attr in request.json:
                setattr(habit, attr, request.json[attr])
            db.session.add(habit)
            db.session.commit()
            return make_response(habit.to_dict(), 202)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(HabitsById, "/habits/<int:id>")

class Users(Resource):
    def get(self):
        users = [user.to_dict(rules = ("-habit_entries",)) for user in User.query.all()]
        return make_response(users, 200)

    def post(self):
        try:
            user = User(
                username = request.json["username"],
                age = request.json["age"],
                _password_hash = request.json["password_hash"],
                image_url = request.json["image_url"]
            )
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 201)
        except:
            return make_response({"error": ["validation error"]}, 400)

api.add_resource(Users, "/users")

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        if not user:
            return make_response({"error": ["user not found"]}, 404)
        return make_response(user.to_dict(), 200)

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
            entry = HabitEntry(
                user_id = request.json["user_id"],
                habit_id = request.json["habit_id"]
            )
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
        entry = HabitEntry.query.filter(Entry.id == id).first()
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

api.add_resource(HabitEntriesById, "/habit_entries/<int:id>")

class Signup(Resource):
    def post(self):
        try:
            new_user = User(
                username = request.json['username'],
                password_hash = request.json['password'],
                age = request.json['age'],
                image_url = fake.image_url()
            )
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return make_response(new_user.to_dict(rules=('-_password_hash',)), 201)
        except ValueError:
            return make_response({"error": "User not created"}, 400)

api.add_resource(Signup, '/signup')
class CheckSession(Resource):

    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return make_response(user.to_dict(), 200)
        else:
            return make_response({'message': '401: Not Authorized'}, 401)

class Login(Resource):
    def post(self):
        user = User.query.filter(User.username == request.json['username']).first()
        password = request.json['password']
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        else:
            return make_response({'error': '401 Unauthorized'}, 401)

api.add_resource(Login, '/login')


api.add_resource(CheckSession, '/check_session')
class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)

api.add_resource(Logout, '/logout')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

