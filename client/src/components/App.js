import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";

import Main from "./Main";
import Signup from "./Signup";
import Login from "./Login";
import NewHabit from "./NewHabit";

function App() {
  const [habits, setHabits] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:5555/daily_habits")
    .then(res => res.json())
    .then(habits => setHabits(habits))
  }, [])

  function handleAddHabit(newhabit) {
      setHabits([...habits, newhabit])
  }

  return (
    <div className="app">
    <Router>
      <Switch>
        <Route exact path="/">
          <Main 
            habits={habits}
            
          />
        </Route>
        <Route exact path="/new_habit">
          <NewHabit 
            habits={habits}
            handleAddHabit={handleAddHabit}

          />
        </Route> 
        <Route exact path="/login">
          <Login
          
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
