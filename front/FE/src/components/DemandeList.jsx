import React, { useEffect, useState } from "react";
import { getDemandes, engagerTache } from "../services/api";

const DemandeList = () => {
  const [demandes, setDemandes] = useState([]);

  useEffect(() => {
    getDemandes().then(res => setDemandes(res.data));
  }, []);

  const handleEngage = (id) => {
    engagerTache(id).then(() => alert("Engagement réussi"));
  };

  return (
    <div>
      <h2>Demandes Disponibles</h2>
      <ul>
        {demandes.map(d => (
          <li key={d.id}>
            {d.description} | Status: {d.status?.etat || "N/A"}
            <button onClick={() => handleEngage(d.id)}>S'engager</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DemandeList;
