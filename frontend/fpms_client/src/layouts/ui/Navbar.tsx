import React from 'react';
import { Link } from 'react-router-dom';
import ThemeToggle from '../ThemeToggle';
import MegaMenu from "./MegaMenu";// Make sure to provide the correct path


const Navbar: React.FC = () => {
    return (
        <div>
        <MegaMenu />
        </div>
     
  );
};

export default Navbar;

