import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/MesDemandes.css"; 
import { FiClock, FiCheckCircle, FiXCircle } from "react-icons/fi";

const MesDemandes = () => {
  const [demandes, setDemandes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchMesDemandes = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/sinistres/mes-demandes", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setDemandes(res.data);
      } catch (err) {
        setError("Erreur lors du chargement de vos demandes.");
      } finally {
        setLoading(false);
      }
    };

    fetchMesDemandes();
  }, []);

  const getStatusBadge = (etat) => {
    switch (etat) {
      case "confirmé":
        return <span className="badge confirmed"><FiCheckCircle /> Confirmée</span>;
      case "rejeté":
        return <span className="badge rejected"><FiXCircle /> Rejetée</span>;
      default:
        return <span className="badge pending"><FiClock /> En attente</span>;
    }
  };

  if (loading) return <p>Chargement...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div className="mes-demandes-container">
      <h2>Mes Demandes</h2>
      {demandes.length === 0 ? (
        <p>Aucune demande trouvée.</p>
      ) : (
        <div className="demandes-list">
          {demandes.map((demande) => (
            <div className="demande-card" key={demande.id}>
              <div className="card-header">
                <h3>{demande.type_aide}</h3>
                {getStatusBadge(demande.status?.etat || "en attente")}
              </div>
              <p className="description">{demande.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MesDemandes;
