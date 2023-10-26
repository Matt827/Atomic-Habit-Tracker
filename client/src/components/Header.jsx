import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

function Header({ onLogout }) {
    function handleLogout() {
        fetch("/logout", {
            method: "DELETE",
          }).then(() => onLogout());
    }

    return (
        <div className='header-container'>
            <h1>Header</h1>
            <Link className="main-button" to="/">
                Main
            </Link>
            <Link className="login-button" to="/login">
                Login
            </Link>
            <Link className="signup-button" to="/signup">
                Signup
            </Link>
            <button onClick={handleLogout}>Logout</button>
        </div>
    )
}

export default Header;