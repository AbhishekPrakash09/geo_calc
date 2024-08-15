import { useEffect } from "react";
import { useLoaderData, useNavigate } from "react-router-dom";

const RootLayout = () => {
  const navigate = useNavigate();
  const isValid = useLoaderData();

  useEffect(() => {
    if (!isValid) {
      navigate("/login");
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
}
