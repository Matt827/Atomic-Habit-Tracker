Atomic Habit Tracker

Description:
Atomic Habit Tracker is a website that helps users measure, quantify, and track their progress to build better habits in various ways.

CRUD:
Create habits and entries to add to database,
Read list of personal habits from database,
Update and edit habits and entries in database,
Delete habits and entries from database

Wireframe:

![Screen Shot 2023-10-24 at 1 54 23 PM](https://github.com/Matt827/Atomic-Habit-Tracker/assets/122830375/ab3a128e-cc6a-449d-b67f-0437724f8de8)

Domain Model:

![Screen Shot 2023-10-24 at 1 56 44 PM](https://github.com/Matt827/Atomic-Habit-Tracker/assets/122830375/e4b62ab6-3123-4737-8edf-b98728b605f7)

Many-to-many relationships:
User has many habits through entries,
Habit has many users through entries,
Entry belongs to a User and a Habit

Validations:
User must have username
Habit must have name
Entry must have a user and habit

Api Routes:

Frontend React Components:
