import React, { useState, useEffect } from 'react'
import { useHistory } from "react-router-dom";
import Header from './Header'

const initialValue ={
	username: '',
	password: '',
}

const Signup = ({userToDisplay, onFormSwitch}) => {
	const [signupForm, setSignupForm] = useState(initialValue)

    const navigate = useHistory()

	function handleSignupChange(e) {
		const name = e.target.name
		const value = e.target.value
		setSignupForm({...signupForm, [name]: value})
	}

	function handleSignupSubmit(e) {
		e.preventDefault()
		fetch('http://127.0.0.1:5555/signup', {
			method: "POST",
			headers: {"Content-Type": "application/json"},
			body: JSON.stringify(signupForm)
		})
		.then(res => res.json())
		.then((user) => {
			userToDisplay(user)
            setSignupForm(initialValue)
            navigate('http://127.0.0.1:5555/')
		})
	}

  return (
	<>
    {/* <Header /> */}
    <div className="auth-container">
		<form className="signup-form" onSubmit={handleSignupSubmit}>
			<label for="username">Username</label>
			<input 
				type="text" 
				autoComplete='off' 
				placeholder="Username" 
				onChange={handleSignupChange} 
				name='username' 
				value ={signupForm.username}  />
			<label for="password">Password</label>
			<input 
				type="password" 
				autoComplete='off' 
				placeholder="Password" 
				onChange={handleSignupChange} 
				name='password' 
				value ={signupForm.password}  />
			<input 
				className="signup-submit"
				type="submit" 
				value="Sign up"/>
		</form>
		<button className="signup-button" onClick={() => onFormSwitch('login')}>Already have an account? Login here.</button>
    </div>
	</>
  )
}

export default Signup