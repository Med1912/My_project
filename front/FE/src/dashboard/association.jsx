import { useEffect, useState } from "react";
import axios from "axios";
import { FiCheck, FiTrash2, FiClock, FiCheckCircle, FiXCircle } from "react-icons/fi";
import "../styles/association.css";  

const Association = () => {
  const [demandes, setDemandes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const token = localStorage.getItem("token");

  const [stats, setStats] = useState({
    total: 0,
    pending: 0,
    confirmed: 0,
    rejected: 0
  });

  useEffect(() => {
    fetchDemandes();
  }, []);

  const fetchDemandes = async () => {
    try {
      setLoading(true);
      const res = await axios.get("http://127.0.0.1:8000/associations/demandes", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setDemandes(res.data);
      calculateStats(res.data);
      setLoading(false);
    } catch (err) {
      setError("Erreur lors du chargement des demandes");
      setLoading(false);
    }
  };

  const calculateStats = (data) => {
    const total = data.length;
    const pending = data.filter(d => d.status?.etat === "en attente").length;
    const confirmed = data.filter(d => d.status?.etat === "confirmé").length;
    const rejected = data.filter(d => d.status?.etat === "rejeté").length;
    
    setStats({
      total,
      pending,
      confirmed,
      rejected
    });
  };

  const updateStatus = async (id, newEtat) => {
    try {
      await axios.patch(
        `http://127.0.0.1:8000/associations/demandes/${id}/confirmer`,
        { etat: newEtat },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      fetchDemandes();
    } catch {
      alert("Erreur lors de la mise à jour du statut");
    }
  };

  const deleteDemande = async (id) => {
    if (!window.confirm("Voulez-vous vraiment supprimer cette demande ?")) return;
    try {
      await axios.delete(`http://127.0.0.1:8000/associations/demandes/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchDemandes();
    } catch {
      alert("Erreur lors de la suppression");
    }
  };

  const getStatusBadge = (etat) => {
    switch(etat) {
      case "confirmé":
        return <span className="badge confirmed"><FiCheckCircle /> Confirmé</span>;
      case "rejeté":
        return <span className="badge rejected"><FiXCircle /> Rejeté</span>;
      default:
        return <span className="badge pending"><FiClock /> En attente</span>;
    }
  };

  if (loading) return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Chargement des données...</p>
    </div>
  );
  
  if (error) return <p className="error-message">{error}</p>;

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Tableau de Bord Association</h1>
        <p className="subtitle">Gestion des demandes d'aide</p>
      </header>

      <div className="stats-container">
        <div className="stat-card total">
          <h3>Total Demandes</h3>
          <p>{stats.total}</p>
        </div>
        <div className="stat-card pending">
          <h3>En Attente</h3>
          <p>{stats.pending}</p>
        </div>
        <div className="stat-card confirmed">
          <h3>Confirmées</h3>
          <p>{stats.confirmed}</p>
        </div>
        <div className="stat-card rejected">
          <h3>Rejetées</h3>
          <p>{stats.rejected}</p>
        </div>
      </div>

      <section className="demandes-section">
        <h2>Liste des Demandes</h2>
        {demandes.length === 0 ? (
          <div className="empty-state">
            <p>Aucune demande disponible pour le moment.</p>
          </div>
        ) : (
          <div className="demandes-grid">
            {demandes.map((demande) => (
              <div key={demande.id} className="demande-card">
                <div className="card-header">
                  <h3>{demande.type_aide}</h3>
                  {getStatusBadge(demande.status?.etat || "en attente")}
                </div>
                
                <div className="card-body">
                  <p className="description">{demande.description}</p>
                  
                  <div className="meta-info">
                    <div className="meta-item">
                      <span className="meta-label">Demandeur:</span>
                      {demande.sinistre?.user?.nom} {demande.sinistre?.user?.prenom}
                    </div>
                  </div>
                </div>

                <div className="card-actions">
                  {demande.status?.etat !== "confirmé" && (
                    <button
                      onClick={() => updateStatus(demande.id, "confirmé")}
                      className="btn-confirm"
                    >
                      <FiCheck /> Confirmer
                    </button>
                  )}
                  {demande.status?.etat !== "rejeté" && (
                    <button
                      onClick={() => updateStatus(demande.id, "rejeté")}
                      className="btn-reject"
                    >
                      <FiXCircle /> Rejeter
                    </button>
                  )}
                  <button
                    onClick={() => deleteDemande(demande.id)}
                    className="btn-delete"
                  >
                    <FiTrash2 /> Supprimer
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};

export default Association;
