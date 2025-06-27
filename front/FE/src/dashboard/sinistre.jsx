import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Sinistre.css";
import Header from "../components/Header";

const Sinistre = () => {
  const [associations, setAssociations] = useState([]);
  const [selectedAssociation, setSelectedAssociation] = useState(null);
  const [typeAide, setTypeAide] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");

  const token = localStorage.getItem("token");

  useEffect(() => {

    console.log("Token in Sinistre:", token);
    if (!token) {
    alert("Token manquante. Veuillez vous connecter.");
    return;
  }
    axios
      .get("http://127.0.0.1:8000/associations/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((res) => setAssociations(res.data))
      .catch((err) =>
        console.error("Erreur de chargement ", err)
      );
  }, []);

  const handleSendDemande = async (e) => {
    e.preventDefault();
    try {
      console.log("token :", token);
      
      await axios.post(
        "http://127.0.0.1:8000/demandes/",
      
        {
          type_aide: typeAide,
          description: description,
          association_id: selectedAssociation.id,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );
      setMessage("Demande envoyee !!!");
      setTypeAide("");
      setDescription("");
      setSelectedAssociation(null);
    } catch (err) {
      // console.error(err);
      // setMessage(" Erreur lors de l'envoi");
      if (err.response) {
        alert("Erreur: " + err.response.data.detail);
        } else {
          alert("Erreur réseau : backend ");
        }

    }
  };
  <pre>{JSON.stringify(associations, null, 2)}</pre>


  return (
    <>
      <Header/>
    <div className="sinistre-container">
      <h1>Associations Disponibles</h1>

      <div className="grid">
        {associations.map((asso) => (
          <div
            key={asso.id}
            className={`card ${
              selectedAssociation?.id === asso.id ? "active" : ""
            }`}
            onClick={() => setSelectedAssociation(asso)}
          >
            <h2> Association :{asso.nom}</h2>
            {asso.location && (
              <p><strong>Localisation:</strong> {asso.location}</p>
            )}
            {/* <p><strong>Email:</strong> {asso.user.email}</p> */}
            <p><strong>Email:</strong> {asso.email}</p>

          </div>
        ))}
      </div>

      {selectedAssociation && (
        <div className="form-container">
          <h2>
            Envoyer une demande à :{" "}
            <span>{selectedAssociation.nom}</span>
          </h2>

          <form onSubmit={handleSendDemande}>
            <label>Type d'aide</label>
            <select
              value={typeAide}
              onChange={(e) => setTypeAide(e.target.value)}
              required
            >
              <option value="">-- Selectionner --</option>
              <option value="Nourriture">Nourriture</option>
              <option value="Vêtements">Vêtements</option>
              <option value="Médicaments">Médicaments</option>
              <option value="Hébergement">Hébergement</option>
              <option value="Transport">Transport</option>
              <option value="Autre">Autre</option>
            </select>

            <label>Description</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            ></textarea>

            <div className="form-actions">
              <button type="submit" className="btn btn-send">
                Envoyer
              </button>
              <button
                type="button"
                className="btn btn-cancel"
                onClick={() => setSelectedAssociation(null)}
              >
                Annuler
              </button>
            </div>
          </form>
        </div>
      )}

      {message && <div className="message">{message}</div>}
    </div>
    </>
  );
};

export default Sinistre;
