import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./forms/Login";
import Register from "./forms/Register";
import MotDePasseOublie from "./forms/MotDePasseOublie";
import Page_Acceuil from './Acceuil/Page_Acceuil';
import Sinistre from "./dashboard/sinistre";
import Association from "./dashboard/association";
import MeDemandes from "./dashboard/MeDemandes";

// Layout avec Header/Nav/Footer
import LayoutAvecHeader from './layouts/LayoutAvecHeader';

function App() {
  return (
    <Router>
      <Routes>

        {/* ✅ Routes SANS Header/Nav/Footer */}
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/MotDePasseOublie" element={<MotDePasseOublie />} />

        {/* ✅ Routes AVEC Header/Nav/Footer */}
        <Route element={<LayoutAvecHeader />}>
          <Route path="/Page_Acceuil" element={<Page_Acceuil />} />
          <Route path="/dashboard/sinistre" element={<Sinistre />} />
          <Route path="/dashboard/association" element={<Association />} />
          <Route path="/dashboard/MeDemandes" element={<MeDemandes />} />
          <Route path="/dashboard/volontaire" element={<h1>Dashboard Volontaire</h1>} />
        </Route>
        
      </Routes>
    </Router>
  );
}

export default App;
