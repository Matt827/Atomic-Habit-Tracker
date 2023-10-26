import React, { useState, useEffect } from 'react'
import { useNavigate } from "react-router-dom";
import Header from './Header'

const initialValue ={
	username: '',
	password: '',
	age: ''
}

const Signup = ({userToDisplay}) => {
	const [signupForm, setSignupForm] = useState(initialValue)

    const navigate = useNavigate()

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
    <Header />
    <div className="singup-container">
			<div>Signup</div>
			<form className="signup-form" onSubmit={handleSignupSubmit}>
				<input 
					type="text" 
					autoComplete='off' 
					placeholder="Username" 
					onChange={handleSignupChange} 
					name='username' 
					value ={signupForm.username}  />
				<input 
					type="text" 
					autoComplete='off' 
					placeholder="Password" 
					onChange={handleSignupChange} 
					name='password' 
					value ={signupForm.password}  />
                <input 
                    className="signup-submit"
                    type="submit" 
                    value="submit"/>
			</form>
    </div>
    </>
  )
}