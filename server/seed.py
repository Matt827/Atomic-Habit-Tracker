#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User, HabitEntry, DailyHabit

fake = Faker()

def create_habits():
    habits = []
    for _ in range(20):
        h = DailyHabit(
            name = fake.name(),
        )
        habits.append(h)
    return habits


def create_users():
    users = []
    for _ in range(5):
        u = User(
            username = fake.user_name(),
        )
        users.append(u)
    return users


def create_entries(users, habits):
    entries = []

    for _ in range(5):
        e = HabitEntry(
            dailyHabit_id = rc(habits).id,
            user_id = rc(users).id
        )
        entries.append(e)
    return entries


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        User.query.delete()
        HabitEntry.query.delete()
        DailyHabit.query.delete()

        print("seeding DailyHabits...")
        habits = create_habits()
        db.session.add_all(habits)
        db.session.commit()

        print("seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("seeding HabitEntries...")
        entries = create_entries(users, habits)
        db.session.add_all(entries)
        db.session.commit()

        print("Done seeding!")