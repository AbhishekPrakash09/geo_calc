import axios from "axios";

const instance = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
      "Content-type": "application/json",
    },
});



instance.interceptors.response.use(
    (response) => response,
    (error) => {
      console.log(error)
    }
);
  
instance.interceptors.request.use(
    (config) => {
      const token = localStorage.getItem("token");
      const refreshToken = localStorage.getItem("refreshToken");
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      if (refreshToken) {
        config.headers.RefreshToken = refreshToken;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
);

export default instance;
  