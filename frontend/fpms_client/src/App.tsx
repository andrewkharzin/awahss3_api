import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ThemeProvider } from "./layouts/ThemeContext";
import { Provider } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";
import Layout from "./layouts/Layout";
import store, { persistor } from "./store";
import routes from "./routes";


const App: React.FC = () => {
  
  
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <ThemeProvider>
          <Router>
            <Layout>
              <Routes>
                {routes.map((route, index) => (
                  <Route
                    key={index}
                    path={route.path}
                    element={<route.component />}
                  />
                ))}
                <Route path="/auth/login " />
                {/* <Route path="/schedules/freighters/gantt" element={<FlightGantt flights={flights} />} /> */}
              </Routes>
            </Layout>
          </Router>
        </ThemeProvider>
      </PersistGate>
    </Provider>
  );
};

export default App;
