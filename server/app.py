#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, abort, session, jsonify

from flask_restful import Resource

# Local imports
from config import app, db, api

# Add Models here
from model import User, Entry, DailyHabit, WeeklyHabit, MonthlyHabit



api = Api(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

