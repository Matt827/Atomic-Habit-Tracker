import React, { useState, useEffect } from 'react';
import Entry from './Entry';

function EntryList({entries}) {
    const displayEntries = entries.map(entry => {
        return <Entry
            key = {entry.id}
            id = {entry.id}
            user_id = {entry.user_id}
            habit_id = {entry.dailyHabit_id}
        />
    })
    return (
        <div className='login-container'>
            <h1>EntryList</h1>
            {displayEntries}
        </div>
    )
}

export default EntryList;