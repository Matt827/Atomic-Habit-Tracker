import React, { useState, useEffect } from 'react';
import Header from './Header';
import HabitList from './HabitList';

function Main() {
    const [habits, setHabits] = useState([])

    useEffect(() => {
      fetch("http://127.0.0.1:5555/daily_habits")
      .then(res => res.json())
      .then(habits => setHabits(habits))
    }, [])

    return (
        <div className='main-container'>
            <Header />
            <h1>Main</h1>
            <HabitList 
                habits={habits}
            />
        </div>
    )
}

export default Main;