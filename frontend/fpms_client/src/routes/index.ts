import { Routes, Route } from "react-router-dom";
import scheduleRoutes from "./modules/schedules";
import privateRoutes from "./modules/ProtectedRoute";

const routes = [
  // ...other routes
  ...scheduleRoutes,
];

export default routes;
