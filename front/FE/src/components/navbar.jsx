import { FiMenu, FiSearch, FiBell, FiChevronDown } from "react-icons/fi";
import './styles/navbar.css';

const Navbar = ({ setMobileNavOpen }) => {
  return (
    <header className="topbar">
      <div className="left-section">
        <button className="menu-btn" onClick={() => setMobileNavOpen(true)}>
          <FiMenu />
        </button>
        <div className="search-bar">
          <FiSearch className="search-icon" />
          <input type="text" placeholder="Rechercher..." />
        </div>
      </div>
      
      <div className="right-section">
        <button className="notification-btn">
          <FiBell />
          <span className="notification-badge">3</span>
        </button>
        
        <div className="user-profile">
          <div className="avatar">A</div>
          <div className="user-details">
            <span className="user-name">Admin Association</span>
            <span className="user-role">Administrateur</span>
          </div>
          <FiChevronDown className="dropdown-icon" />
        </div>
      </div>
    </header>
  );
};

export default Navbar;