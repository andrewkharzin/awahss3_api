import { useNavigate, RouteProps } from "react-router";
import { useSelector } from "react-redux";
import { RootState } from "../../store";

const ProtectedRoute = (props: RouteProps) => {
  const auth = useSelector((state: RootState) => state.auth);
  const navigate = useNavigate();

  if (auth.account) {
    if (props.path === "/") {
      return navigate("/");
    }
    return navigate("/profile");
  } else if (!auth.account) {
    return navigate("/auth/login");
  }
};

export default ProtectedRoute;
