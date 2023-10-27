import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

import Header from './Header';
import HabitList from './HabitList';
import Signup from './Signup';
import Login from './Login';

function Main({habits, onLogout, user_id}) {
    const [currentForm, setCurrentForm] = useState("login")

    const toggleForm = (formName) => {
        setCurrentForm(formName)
    }

    return (
        <div className='main-container'>
            {
                currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Signup onFormSwitch={toggleForm}/>
            }
            {/* <Header onLogout={onLogout}/>
            <h1>Main</h1>
            <div className='month'>

            </div>
            <div className="daily-habits">
                <HabitList habits={habits}/>

            </div>
            <div className="weekly-habits">

            </div>
            <div className="monthly-habits">

            </div>
            <button>
                <Link className="new-habit-button" to="/new_habit">
                    Add new habit
                </Link>
            </button> */}
        </div>
    )
}

export default Main;