    import React from 'react';
import { Outlet } from 'react-router-dom';
import Header from '../Acceuil/Header';
import Nav_bar from '../Acceuil/Nav_bar';
import Footer from '../Acceuil/Footer';

export default function LayoutAvecHeader() {
  return (
    <div className="app-layout">
      <Header />
      <div className="content-wrapper">
        <Nav_bar />
        <main className="main-content">
          <Outlet /> {/* c’est ici que s’affiche la page */}
        </main>
      </div>
      <Footer />
    </div>
  );
}
