import React, { useState, useEffect } from 'react';

function Habit({name, handleAddHabit}) {

    return (
        <div className='habit-container' onClick={handleAddHabit}>
            <h3>{name}</h3>
        </div>
    )
}

export default Habit;