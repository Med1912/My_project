import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import API from '../../api'; 
import './Login.css';
import NavBarSimple from '../Acceuil/NavBarSimple';  // ✅ Chemin correct si le fichier est là

export default function Register() {
  const [formData, setFormData] = useState({
    nom: '',
    prenom: '',
    email: '',
    password: '',
    role: '',
    association_nom: '',
    latitude: null,
    longitude: null,
  });

  const [message, setMessage] = useState({ text: '', type: '' });
  const navigate = useNavigate();

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateEmail(formData.email)) {
      setMessage({ text: 'Veuillez entrer une adresse email valide', type: 'error' });
      return;
    }

    if (formData.password.length < 6) {
      setMessage({ text: 'Le mot de passe doit contenir au moins 6 caractères', type: 'error' });
      return;
    }

    try {
      await API.post('/users/register', formData);
      setMessage({ text: 'Inscription réussie ! Redirection...', type: 'success' });

      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (error) {
      console.error('Erreur:', error.response?.data || error.message);
      setMessage({ text: "Erreur d'inscription", type: 'error' });
    }
  };

  return (
    <>
      {/* ✅ Affiche la nav-bar simple ici */}
      <NavBarSimple />

      <div className="login-container">
        <div className="login-header">
          <h1>Créer un compte</h1>
          <p>Rejoignez notre communauté</p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <input
              type="text"
              name="nom"
              value={formData.nom}
              onChange={handleChange}
              placeholder=""
              required
            />
            <label>Nom</label>
          </div>

          <div className="input-group">
            <input
              type="text"
              name="prenom"
              value={formData.prenom}
              onChange={handleChange}
              placeholder=""
              required
            />
            <label>Prénom</label>
          </div>

          <div className="input-group">
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder=""
              required
            />
            <label>Email</label>
          </div>

          <div className="input-group">
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder=""
              required
            />
            <label>Mot de passe</label>
          </div>

          <div className="Type_inscription">
            <select name="role" value={formData.role} onChange={handleChange} required>
              <option value="" disabled>Que vous êtes vous ?</option>
              <option value="association">Association</option>
              <option value="volontaire">Volontaire</option>
              <option value="sinistre">Sinistré</option>
            </select>
          </div>

          {formData.role === 'association' && (
            <div className="input-group">
              <input
                type="text"
                name="association_nom"
                value={formData.association_nom}
                onChange={handleChange}
                placeholder=""
                required
              />
              <label>Nom de l'association</label>
            </div>
          )}

          <button type="submit" className="login-button">S'inscrire</button>

          {message.text && (
            <div className={`${message.type}-message`}>{message.text}</div>
          )}

          <div className="signup-link">
            Déjà un compte ? <Link to="/login">Se connecter</Link>
          </div>
        </form>
      </div>
    </>
  );
}
