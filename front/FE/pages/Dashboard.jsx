import React from "react";
import AssociationList from "../components/AssociationList";
import DemandeList from "../components/DemandeList";
import TachesList from "../components/TachesList";

const Dashboard = () => {
  return (
    <div>
      <h1>Bienvenue Volontaire</h1>
      <AssociationList />
      <DemandeList />
      <TachesList />
    </div>
  );
};

export default Dashboard;
