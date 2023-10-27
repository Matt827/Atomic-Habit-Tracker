import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"
import Habit from "./Habit"
import Header from './Header';

function NewHabit({habits, user_id, handleAddHabit}) {
    const displayHabits = habits.map(habit => {
        return <Habit
            key = {habit.id}
            name = {habit.name}
            duration = {habit.duration}
            daily = {habit.daily}
            weekly = {habit.weekly}
            monthly = {habit.monthly}
            yearly = {habit.yearly}
            users = {habit.users}
            user_id = {user_id}
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
                    Custom Habit
                </Link>
            </button>
        </div>
    )
}

export default NewHabit;