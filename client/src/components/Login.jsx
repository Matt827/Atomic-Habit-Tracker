import React, { useState, useEffect } from 'react';
import Header from './Header';

function Login({ onLogin }) {
    const [username, setUsername] = useState("");
  
    function handleSubmit(e) {
      e.preventDefault();
      fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username }),
      })
        .then((r) => r.json())
        .then((user) => onLogin(user));
    }
  
    return (
        <div className='login-container'>
            <Header />
            <form onSubmit={handleSubmit}>
                <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
  }

export default Login;