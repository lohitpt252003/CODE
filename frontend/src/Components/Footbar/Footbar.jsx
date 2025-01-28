import React from 'react';
// import './Footbar.css'; // Import the CSS file

function Footbar() {
  return (
    <footer className="Footbar-footbar">
      <div className="Footbar-content">
        <p className="Footbar-text">&copy; 2025 MyApp. All rights reserved.</p>
        <ul className="Footbar-links">
          <li className="Footbar-item"><a href="/privacy" className="Footbar-link">Privacy Policy</a></li>
          <li className="Footbar-item"><a href="/terms" className="Footbar-link">Terms of Service</a></li>
          <li className="Footbar-item"><a href="/contact" className="Footbar-link">Contact Us</a></li>
        </ul>
      </div>
    </footer>
  );
}

export default Footbar;