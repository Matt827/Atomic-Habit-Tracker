import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";

import Main from "./Main";
import Signup from "./Signup";
import Login from "./Login";

function App() {
  return (
    <div className="app">
    <Router>
      <Switch>
        <Route exact path="/">
          <Main 
          
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
