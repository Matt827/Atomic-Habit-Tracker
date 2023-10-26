#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User, HabitEntry, Habit, EntryDate

fake = Faker()

def create_habits():
    habits = []

    # Body
    h1 = Habit(name = "Walk", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h1)
    h2 = Habit(name = "Run", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h2)
    h3 = Habit(name = "Strech", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h3)
    h4 = Habit(name = "Exercise", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h4)
    h5 = Habit(name = "Stand", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h5)

    # Mind
    h6 = Habit(name = "Meditation", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h6)
    h7 = Habit(name = "Read a book", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h7)
    h8 = Habit(name = "Study", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h8)
    h9 = Habit(name = "Breathe", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h9)
    h10 = Habit(name = "Review Today", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h10)

    # Health
    h11 = Habit(name = "Drink Water", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h11)
    h12 = Habit(name = "Eat Breakfast", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h12)
    h13 = Habit(name = "Eat Vegtables", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h13)
    h14 = Habit(name = "Sleep Early", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h14)
    h15 = Habit(name = "No Sweets", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h15)

    # Lifestyle
    h16 = Habit(name = "Call Parents", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h16)
    h17 = Habit(name = "Contact a Friend", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h17)
    h18 = Habit(name = "Save Money", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h18)
    h19 = Habit(name = "Track Expenses", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h19)
    h20 = Habit(name = "Journal", daily=False, weekly=False, monthly=False, yearly=False,)
    habits.append(h20)

    return habits

def create_users():
    users = []
    for _ in range(5):
        u = User(
            username = fake.user_name(),
            age = randint(18, 90),
            _password_hash = fake.password(),
            image_url = fake.image_url()
        )
        users.append(u)
    return users

def create_entry_dates(habit_entries):
    entry_dates = []
    for _ in range(5):
        e = EntryDate(
            entry_performed_date = "10/25/2023",
            entry_id = rc(habit_entries).id,
        )
        entry_dates.append(e)
    return entry_dates


def create_entries(users, habits):
    entries = []
    for _ in range(5):
        e = HabitEntry(
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
        Habit.query.delete()
        EntryDate.query.delete()
        HabitEntry.query.delete()

        print("seeding Habits...")
        habits = create_habits()
        db.session.add_all(habits)
        db.session.commit()

        print("seeding Users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("seeding HabitEntries...")
        entries = create_entries(users, habits)
        db.session.add_all(entries)
        db.session.commit()

        print("seeding EntryDates...")
        entry_dates = create_entry_dates(entries)
        db.session.add_all(entry_dates)
        db.session.commit()

        print("Done seeding!")