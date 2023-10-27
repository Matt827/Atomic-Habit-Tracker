import React, { useState, useEffect } from 'react';
import Header from './Header';

function Login({ onLogin, onFormSwitch }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
  
    function handleSubmit(e) {
      e.preventDefault();
      fetch("http://127.0.0.1:5555/login", {
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
		<>
        {/* <Header /> */}
        <div className='auth-container'>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor='Username'>Username</label>
					<input
					type="text"
					placeholder="Username"
					id="Username"
					value={username}
					onChange={(e) => setUsername(e.target.value)}/>
                <label htmlFor='Password'>Password</label>
				<input
					type="password"
					placeholder="Password"
					id="Password"
					value={password}
					onChange={(e) => setPassword(e.target.value)}/>
                <input 
                    className="login-submit"
                    type="submit" 
                    value="Login"/>
            </form>
			<button className="login-button" onClick={() => onFormSwitch('signup')}>Don't have an account? Sign up here.</button>
        </div>
		</>
    );
  }

export default Login;