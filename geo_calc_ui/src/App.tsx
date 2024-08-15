import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./App.css";
import Login from "./pages/Login";
import RootLayout from "./pages/RootLayout";

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
    path: "/",
    children: [
      {
        index: true,
        element: <RootLayout />,
      },
    ],
  },
]);

function App() {
  document.title = "Geo Calc";
  return <RouterProvider router={router} />;
}

export default App;
