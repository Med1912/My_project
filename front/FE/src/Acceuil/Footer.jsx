import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer-container">
      <div className="footer-content">
        <p>© 2023 Nom de l'Association. Tous droits réservés.</p>
        <div className="footer-links">
          <a href="#">Mentions légales</a>
          <a href="#">Contact</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;