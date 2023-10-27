import React, { useState, useEffect } from 'react';

function Habit({name, duration, daily, weekly, monthly, yearly, users, user_id, handleAddHabit}) {
    const [user, setUser] = useState(1)

    function onAddHabit() {
        const newHabit = {
            name: name,
            duration: duration,
            daily: daily,
            weekly: weekly,
            monthly: monthly,
            yearly: yearly,
            users: users,
            handleAddHabit: handleAddHabit
        }
        handleAddHabit(newHabit)

        fetch(`http://127.0.0.1:5555/users/${user}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newHabit),
        })
        .then(res => res.json())
        .then(data => console.log(data))
    }

    return (
        <div className='habit-container' onClick={onAddHabit}>
            <h3>{name}</h3>
        </div>
    )
}

export default Habit;