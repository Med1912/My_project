import React, { useEffect, useState } from "react";
import { getAssociations } from "../../api";

const AssociationList = () => {
  const [associations, setAssociations] = useState([]);

  useEffect(() => {
    getAssociations().then(res => setAssociations(res.data));
  }, []);

  return (
    <div>
      <h2>Associations</h2>
      <ul>
        {associations.map(a => (
          <li key={a.id}>{a.nom} - {a.location}</li>
        ))}
      </ul>
    </div>
  );
};

export default AssociationList;
