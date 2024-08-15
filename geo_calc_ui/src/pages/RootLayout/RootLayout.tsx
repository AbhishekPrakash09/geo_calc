import { useEffect } from "react";
import { useLoaderData, useNavigate } from "react-router-dom";
import { validateToken } from "../../http/auth";

const RootLayout = () => {
  const navigate = useNavigate();
  const isValid = useLoaderData();

  useEffect(() => {
    if (!isValid) {
      navigate("/login");
    } else {
      navigate("/geocalc");
    }
  }, []);
  return <div>RootLayout</div>;
};

export default RootLayout;

export function loader() {
  const token = localStorage.getItem("token");
  if (!token) {
    return false;
  }
  const isValid = validateToken();
  return isValid;
}
