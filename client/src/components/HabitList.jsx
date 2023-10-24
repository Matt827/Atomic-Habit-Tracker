import React, { useState, useEffect } from 'react';
import Habit from './Habit';

function HabitList({habits}) {
    const displayHabits = habits.map(habit => {
        return <Habit
            key = {habit.id}
            name = {habit.name}
        />
    })
    return (
        <div className='login-container'>
            <h1>HabitList</h1>
            {displayHabits}
        </div>
    )
}

export default HabitList;