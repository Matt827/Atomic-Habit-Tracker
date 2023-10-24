import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

import Header from './Header';
import HabitList from './HabitList';
import NewHabit from './NewHabit';

function Main({habits}) {

    return (
        <div className='main-container'>
            <Header />
            <h1>Main</h1>
            <HabitList 
                habits={habits}
            />
            <button>
                <Link className="new-habit-button" to="/new_habit">
                    Add new habit
                </Link>
            </button>
        </div>
    )
}

export default Main;