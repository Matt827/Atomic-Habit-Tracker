import React, { useState, useEffect } from 'react';

function Entry({id, user_id, habit_id}) {

    return (
        <div className='habit-container'>
            <h3>id:{id}, user:{user_id}, habit:{habit_id}</h3>
        </div>
    )
}

export default Entry;