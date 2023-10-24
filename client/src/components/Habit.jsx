import React, { useState, useEffect } from 'react';

function Habit({name}) {

    return (
        <div className='habit-container'>
            <h3>{name}</h3>
        </div>
    )
}

export default Habit;