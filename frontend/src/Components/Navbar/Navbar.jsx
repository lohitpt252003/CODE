import React from 'react';
// import './Navbar.css'; // Import the CSS file

function Navbar() {
  return (
    <nav className="Navbar-navbar">
      <a className="Navbar-logo" href='/'>MyApp</a>
      <ul className="Navbar-links">
        <li className="Navbar-item"><a href="/problems" className="Navbar-link">Problems</a></li>
        <li className="Navbar-item"><a href="/contests" className="Navbar-link">Contests</a></li>
        <li className="Navbar-item"><a href="/about" className="Navbar-link">About</a></li>
        <li className="Navbar-item"><a href="/contact" className="Navbar-link">Contact</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;