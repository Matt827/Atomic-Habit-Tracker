import React, { useState, useEffect } from 'react';
import Habit from './Habit';

function HabitList({habits}) {
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
        />
    })
    return (
        <div className='login-container'>
            {displayHabits}
        </div>
    )
}

export default HabitList;