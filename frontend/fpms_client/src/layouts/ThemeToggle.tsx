import React from 'react';
import { useTheme } from './ThemeContext';

const ThemeToggle: React.FC = () => {
  const { darkMode, toggleDarkMode } = useTheme();

  return (
    <div className="theme-toggle">
      <label className="theme-toggle__label" htmlFor="darkModeToggle">
        Dark Mode
      </label>
      <input
        type="checkbox"
        id="darkModeToggle"
        className="theme-toggle__checkbox"
        checked={darkMode}
        onChange={toggleDarkMode}
      />
    </div>
  );
};

export default ThemeToggle;
