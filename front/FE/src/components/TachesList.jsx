import React, { useEffect, useState } from "react";
import { getMesTaches } from "../services/api";

const TachesList = () => {
  const [taches, setTaches] = useState([]);

  useEffect(() => {
    getMesTaches().then(res => setTaches(res.data));
  }, []);

  return (
    <div>
      <h2>Mes Tâches</h2>
      <ul>
        {taches.map(t => (
          <li key={t.id}>{t.description} - {t.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default TachesList;
