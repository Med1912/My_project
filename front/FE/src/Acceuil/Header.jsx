import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <img 
        src="/assets/logo-spana.jpg" 
        alt="Logo SPANA" 
        className="logo"
      />
    </header>
  );
};

export default Header;