import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

const MotDePasseOublie = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState({ text: '', type: '' });
  const [etape, setEtape] = useState(1);

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validateEmail(email)) {
      setMessage({ text: 'Veuillez entrer une adresse email valide', type: 'error' });
      return;
    }

    setTimeout(() => {
      setMessage({ 
        text: 'Un lien de réinitialisation a été envoyé à votre adresse email', 
        type: 'success' 
      });
      setEtape(2);
    }, 1000);
  };

  return (
    <div className="login-container">
      <div className="login-header">
        <h1>Récupération de mot de passe</h1>
        <p>
          {etape === 1 
            ? "Entrez votre email pour recevoir un lien de réinitialisation" 
            : "Vérifiez votre boîte mail"}
        </p>
      </div>

      {etape === 1 ? (
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder=" "
              required
            />
            <label htmlFor="email">Adresse Email</label>
          </div>

          <button type="submit" className="login-button">
            Envoyer le lien
          </button>

          {message.text && (
            <div className={`${message.type}-message`}>
              {message.text}
            </div>
          )}
        </form>
      ) : (
        <div className="confirmation-message">
          <p>Consultez l'email envoyé à <strong>{email}</strong> pour réinitialiser votre mot de passe.</p>
        </div>
      )}

      <div className="signup-link">
        <Link to="/login">Retour à la connexion</Link>
      </div>
    </div>
  );
};

export default MotDePasseOublie;