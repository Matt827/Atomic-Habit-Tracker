#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User, Entry, Habit

fake = Faker()

def create_habits():
    habits = []

    # Body
    h1 = Habit(name = "Walk")
    habits.append(h1)
    h2 = Habit(name = "Run")
    habits.append(h2)
    h3 = Habit(name = "Strech")
    habits.append(h3)
    h4 = Habit(name = "Exercise")
    habits.append(h4)
    h5 = Habit(name = "Stand")
    habits.append(h5)

    # Mind
    h6 = Habit(name = "Meditation")
    habits.append(h6)
    h7 = Habit(name = "Read a book")
    habits.append(h7)
    h8 = Habit(name = "Study")
    habits.append(h8)
    h9 = Habit(name = "Breathe")
    habits.append(h9)
    h10 = Habit(name = "Review Today")
    habits.append(h10)

    # Health
    h11 = Habit(name = "Drink Water")
    habits.append(h11)
    h12 = Habit(name = "Eat Breakfast")
    habits.append(h12)
    h13 = Habit(name = "Eat Vegtables")
    habits.append(h13)
    h14 = Habit(name = "Sleep Early")
    habits.append(h14)
    h15 = Habit(name = "No Sweets")
    habits.append(h15)

    # Lifestyle
    h16 = Habit(name = "Call Parents")
    habits.append(h16)
    h17 = Habit(name = "Contact a Friend")
    habits.append(h17)
    h18 = Habit(name = "Save Money")
    habits.append(h18)
    h19 = Habit(name = "Track Expenses")
    habits.append(h19)
    h20 = Habit(name = "Journal")
    habits.append(h20)

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
        e = Entry(
            habit_id = rc(habits).id,
            user_id = rc(users).id
        )
        entries.append(e)
    return entries


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        User.query.delete()
        Entry.query.delete()
        Habit.query.delete()

        print("seeding Habits...")
        habits = create_habits()
        db.session.add_all(habits)
        db.session.commit()

        print("seeding Users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("seeding Entries...")
        entries = create_entries(users, habits)
        db.session.add_all(entries)
        db.session.commit()

        print("Done seeding!")