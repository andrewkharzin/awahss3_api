import React from "react";
import { Route, useNavigate, RouteProps, Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { RootState } from "../../store";

const ProtectedRoute = (props: RouteProps) => {
  const auth = useSelector((state: RootState) => state.auth);
  const navigate = useNavigate()

  if (auth.account) {
    if (props.path === "/auth/login") {
      return navigate('/');
    }
    
  } else if (!auth.account) {
    return navigate("/login");
  } 
};

export default ProtectedRoute;
