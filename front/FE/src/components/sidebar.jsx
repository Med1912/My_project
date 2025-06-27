import { FiHome, FiUsers, FiFileText, FiSettings, FiLogOut } from "react-icons/fi";
import './styles/sidebar.css';

const Sidebar = ({ mobileNavOpen, setMobileNavOpen }) => {
  return (
    <nav className={`sidebar ${mobileNavOpen ? 'open' : ''}`}>
      <div className="sidebar-header">
        <h2>Association</h2>
        <button className="close-nav" onClick={() => setMobileNavOpen(false)}>
          <FiX />
        </button>
      </div>
      
      <ul className="nav-links">
        <li className="active">
          <FiHome />
          <span>Tableau de bord</span>
        </li>
        <li>
          <FiUsers />
          <span>Bénéficiaires</span>
        </li>
        <li>
          <FiFileText />
          <span>Demandes</span>
        </li>
        <li>
          <FiSettings />
          <span>Paramètres</span>
        </li>
      </ul>
      
      <div className="logout-btn" onClick={handleLogout}>
        <FiLogOut />
        <span>Déconnexion</span>
      </div>
    </nav>
  );
};

export default Sidebar;