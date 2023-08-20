import React, { useState } from 'react';

interface TabPanelProps {
  tabs: string[];
  children: React.ReactNode[];
}

const TabPanel: React.FC<TabPanelProps> = ({ tabs, children }) => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div className="space-y-2">
      <div className="border-b border-gray-300 dark:border-gray-700">
        <nav className="flex -mb-px space-x-4">
          {tabs.map((tab, index) => (
            <button
              key={index}
              className={`px-4 py-2 text-sm font-medium ${
                activeTab === index
                  ? 'border-b-2 border-indigo-500 dark:border-indigo-400 text-indigo-600 dark:text-indigo-400'
                  : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'
              }`}
              onClick={() => setActiveTab(index)}
            >
              {tab}
            </button>
          ))}
        </nav>
      </div>
      <div className="p-4">{children[activeTab]}</div>
    </div>
  );
};

export default TabPanel;
