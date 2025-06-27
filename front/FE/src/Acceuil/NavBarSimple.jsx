import React from 'react';
import { useNavigate } from 'react-router-dom';
import './NavBarSimple.css';

export default function NavBarSimple() {
  const navigate = useNavigate();

  return (
    <header className="navbar-header">
      <div className="logo-container">
        <img src="/logo.png" alt="Logo" className="logo" /> {/* tu peux remplacer "/logo.png" par ton chemin exact */}
      </div>
      <div className="btn-container">
        <button className="home-btn" onClick={() => navigate('/Page_Acceuil')}>
          Accueil
        </button>
      </div>
    </header>
  );
}
