import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./App.css";
import Login from "./pages/Login";
import RootLayout, { loader as rootLoader } from "./pages/RootLayout";
import Registration from "./pages/Registration";

const router = createBrowserRouter([
  {
    path: "/login",
    children: [
      {
        index: true,
        element: <Login />,
      },
    ],
  },
  {
    path: "/register",
    children: [
      {
        index: true,
        element: <Registration />,
      },
    ],
  },
  {
    path: "/",
    element: <RootLayout />,
    loader: rootLoader,
  },
]);

function App() {
  document.title = "Geo Calc";
  return <RouterProvider router={router} />;
}

export default App;
