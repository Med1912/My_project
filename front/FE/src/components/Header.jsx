import React from "react";
import { useNavigate } from "react-router-dom";
import "./Header.css";

const Header = () => {
  const navigate = useNavigate();
  const role = localStorage.getItem("role");
  const email = localStorage.getItem("email");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <nav className="navbar">
        <div className="navbar-left">
      <div className="navbar-logo">Aide Humanitaire</div>
    </div>

      <ul className="navbar-links">
        <li className="navbar-accueil" onClick={() => navigate("/")}>Accueil</li>

        {role === "sinistre" && (
           <li onClick={() => navigate("/dashboard/MeDemandes")}>Mes demandes</li>
           
        )}
      
        <li onClick={handleLogout}>Déconnexion</li>
      </ul>

      <div className="navbar-user">{email}</div>
    </nav>
  );
};

export default Header;
