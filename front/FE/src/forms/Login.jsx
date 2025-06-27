import React, { useState } from "react";
import API from "../../api";
import { useNavigate } from "react-router-dom";
import "./Login.css";
import "./MotDePasseOublie";

export default function Login() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.email || !form.password) {
      setError("Tous les champs sont requis.");
      return;
    }

    try {
      const res = await API.post("/users/login", form);
      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("user", JSON.stringify(res.data.user));
      localStorage.setItem("role", res.data.user.role);
      const role = res.data.user.role.toLowerCase();
      if (role === "association") navigate("/dashboard/association");
      else if (role === "volontaire") navigate("/dashboard/volontaire");
      else if (role === "sinistre") navigate("/dashboard/sinistre");
      else navigate("/");
    } catch (err) {
      setError("Email ou mot de passe incorrect !");
      console.log("Login error:", err.response ? err.response.data : err.message);
    }
  };

  return (
    <div className="login-container">
      <div className="login-header">
        <h1>Bienvenue</h1>
        <p>Connectez-vous à votre compte</p>
      </div>

      <form onSubmit={handleSubmit} className="login-form">
        <div className="input-group">
          <input
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            placeholder=" "
            required
            autoComplete="email"
          />
          <label htmlFor="email">Adresse Email</label>
        </div>

        <div className="input-group">
          <input
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            placeholder=" "
            required
            autoComplete="current-password"
          />
          <label htmlFor="password">Mot de passe</label>
        </div>

        <div className="forgot-password">
          <a href="/MotDePasseOublie">Mot de passe oublié ?</a>
        </div>

        <button type="submit" className="login-button">Se connecter</button>

        {error && <div className="error-message">{error}</div>}

        <div className="signup-link">
          Pas de compte ? <a href="/Register">S'inscrire</a>
        </div>
      </form>
    </div>
  );
}
