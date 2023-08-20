
import './index.css';
import { Provider } from 'react-redux';
import { createRoot } from 'react-dom/client';
import React from 'react';
import App from './App';
import store from './store/store'


const container = document.getElementById('root');

if (container) {
  const root = createRoot(container); 
  root.render(
    <Provider store={store}>
      <App />
    </Provider>
  );
} else {
  console.error("Couldn't find container element with ID 'app'");
}
