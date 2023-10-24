import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"
import Habit from "./Habit"
import Header from './Header';

function NewHabit({habits, handleAddHabit}) {
    const displayHabits = habits.map(habit => {
        return <Habit
            key = {habit.id}
            name = {habit.name}
            handleAddHabit = {handleAddHabit}
        />
    })

    return (
        <div className='new-habit-container'>
            <Header />
            <h1>New Habit</h1>
            {displayHabits}
            <button>
                <Link className="custom-habit-button" to="/custom_habit">
                    edit new habit
                </Link>
            </button>
        </div>
    )
}

export default NewHabit;