<h2>Atomic Habit Tracker</h2>

<h3>Description:</h3>

> Atomic Habit Tracker is a website that helps users measure, quantify, and track their progress to build better habits in various ways.

<h3>CRUD:</h3>

* Create habits and entries to add to database
* Read list of personal habits from database
* pdate and edit habits and entries in database
* Delete habits and entries from database

<h3>Wireframe:</h3>

![Screen Shot 2023-10-24 at 1 54 23 PM](https://github.com/Matt827/Atomic-Habit-Tracker/assets/122830375/ab3a128e-cc6a-449d-b67f-0437724f8de8)

<h3>Domain Model:</h3>

![Screen Shot 2023-10-25 at 11 25 25 AM](https://github.com/Matt827/Atomic-Habit-Tracker/assets/122830375/7f4c9b66-6f4c-482d-8d30-50ce55eb7956)


<h3>Many-to-many relationships:</h3>

* User has many habits through entries
* Habit has many users through entries
* Entry belongs to a User and a Habit

<h3>Validations:</h3>

* User must have username
* Habit must have name
* Entry must have a user and habit

<h3>Api Routes:</h3>

* GET/habits
* POST/habits
* GET/habits/<int:id>
* PATCH/habits/<int:id>
* DELETE/habits/<int:id>
* GET/users
* POST/users
* GET/users/<int:id>
* PATCH/users/<int:id>
* DELETE/users/<int:id>
* GET/entries
* POST/entries
* GET/entries/<int:id>
* PATCH/entries/<int:id>
* DELETE/entries/<int:id>


<h3>Frontend React Components:</h3>

* Main: sends a GET request to /habits
* Main: can send POST request to /entry
* Main: can send DELETE request to /entry/<int:id>
* NewHabit: sends a POST request to /habits
* Signup: sends a POST request to /user
* Login: sends a GET request to /user/<int:id>