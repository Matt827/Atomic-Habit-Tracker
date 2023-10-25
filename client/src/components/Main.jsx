import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

import Header from './Header';
import HabitList from './HabitList';
import EntryList from './EntryList';

function Main({habits, entries}) {

    return (
        <div className='main-container'>
            <Header />
            <h1>Main</h1>
            {/* <HabitList  */}
                {/* habits={habits} */}
            {/* /> */}
            <EntryList 
                entries={entries}
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