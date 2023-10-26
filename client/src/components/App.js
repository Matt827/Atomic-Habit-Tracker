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
  const [user, setUser] = useState(null)

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

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session")
    .then((res) => {
      if (res.ok) {
        res.json().then((user) => setUser(user));
      }
    })
  }, [])

  // if (user) {
  //   return <h2>Welcome, {user.username}!</h2>;
  // } else {
  //   return <Login onLogin={setUser} />;
  // }


  function handleAddHabit(newhabit) {
    console.log("Adding habit")
      // setHabits([...habits, newhabit])
  }

  function handleLogin() {
    // onLogin callback function would handle saving the logged in user's details in state
    "pass"
  }

  function handleLogout() {
    // The handleLogout function would handle removing the information about the user from state
    "pass"
  }

  return (
    <div className="app">
    <Router>
      <Switch>
        <Route exact path="/">
          <Main 
            // habits={habits}
            entries={entries}
            onLogout={handleLogout}
            
          />
        </Route>
        <Route exact path="/new_habit">
          <NewHabit 
            habits={habits}
            handleAddHabit={handleAddHabit}

          />
        </Route>
        <Route exact path="/custom_habit">
          <CustomHabit 

          />
        </Route> 
        <Route exact path="/login">
          <Login
            onLogin={handleLogin}
          />
        </Route>
        <Route exact path="/signup">
          <Signup
          
          />
          </Route>
      </Switch>
    </Router>
  </div>
  )
}

export default App;
