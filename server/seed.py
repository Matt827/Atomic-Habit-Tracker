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

# def create_habits():
#     habits = []
#     for _ in range(20):
#         h = DailyHabit(
#             name = fake.name(),
#         )
#         habits.append(h)
#     return habits
def create_habits():
    habits = []

    # Body
    h1 = DailyHabit(name = "Walk")
    habits.append(h1)
    h2 = DailyHabit(name = "Run")
    habits.append(h2)
    h3 = DailyHabit(name = "Strech")
    habits.append(h3)
    h4 = DailyHabit(name = "Exercise")
    habits.append(h4)
    h5 = DailyHabit(name = "Stand")
    habits.append(h5)

    # Mind
    h6 = DailyHabit(name = "Meditation")
    habits.append(h6)
    h7 = DailyHabit(name = "Read a book")
    habits.append(h7)
    h8 = DailyHabit(name = "Study")
    habits.append(h8)
    h9 = DailyHabit(name = "Breathe")
    habits.append(h9)
    h10 = DailyHabit(name = "Review Today")
    habits.append(h10)

    # Health
    h11 = DailyHabit(name = "Drink Water")
    habits.append(h11)
    h12 = DailyHabit(name = "Eat Breakfast")
    habits.append(h12)
    h13 = DailyHabit(name = "Eat Vegtables")
    habits.append(h13)
    h14 = DailyHabit(name = "Sleep Early")
    habits.append(h14)
    h15 = DailyHabit(name = "No Sweets")
    habits.append(h15)

    # Lifestyle
    h16 = DailyHabit(name = "Call Parents")
    habits.append(h16)
    h17 = DailyHabit(name = "Contact a Friend")
    habits.append(h17)
    h18 = DailyHabit(name = "Save Money")
    habits.append(h18)
    h19 = DailyHabit(name = "Track Expenses")
    habits.append(h19)
    h20 = DailyHabit(name = "Journal")
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