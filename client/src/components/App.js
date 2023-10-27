import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";

import Main from "./Main";
import Signup from "./Signup";
import Login from "./Login";
import NewHabit from "./NewHabit";
import CustomHabit from "./CustomHabit";

function App() {
  const [habits, setHabits] = useState([])
  const [entries, setEntries] = useState([])
  const [user, setUser] = useState(1)
  const [currentForm, setCurrentForm] = useState("login")

  const toggleForm = (formName) => {
      setCurrentForm(formName)
  }

  useEffect(() => {
    fetch("http://127.0.0.1:5555/habits")
    .then(res => res.json())
    .then(habits => setHabits(habits))
  }, [])

  useEffect(() => {
    fetch("http://127.0.0.1:5555/habit_entries")
    .then(res => res.json())
    .then(entries => setEntries(entries))
  }, [])


  function handleAddHabit(newhabit) {
    filteredHabits.push(newhabit)
  }

  function handleLogin() {
    // onLogin callback function would handle saving the logged in user's details in state
    "pass"
  }

  function handleLogout() {
    // The handleLogout function would handle removing the information about the user from state
    "pass"
  }

  const filteredHabits = habits.filter(habit => habit.id == user)

  return (
    <div className="app">
    <Router>
      <Switch>
        <Route exact path="/">
          <Main 
            habits={filteredHabits}
            user_id={user}
            onLogout={handleLogout}
            
          />
        </Route>
        <Route exact path="/new_habit">
          <NewHabit 
            habits={habits}
            user_id={user}
            handleAddHabit={handleAddHabit}

          />
        </Route>
        <Route exact path="/custom_habit">
          <CustomHabit 

          />
        </Route> 
        <Route exact path="/login">
          <Login
            onFormSwitch={toggleForm}
            onLogin={handleLogin}
          />
        </Route>
        <Route exact path="/signup">
          <Signup
            onFormSwitch={toggleForm}
          />
          </Route>
      </Switch>
    </Router>
  </div>
  )
}

export default App;
