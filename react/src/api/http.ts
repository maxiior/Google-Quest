import axios from "axios";
import { endpoints } from "routes";

const http = axios.create({
  baseURL: endpoints.HOST,
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
  },
  withCredentials: true,
});

http.interceptors.response.use(
  (response) => response,
  async (error) => {
    return Promise.reject(error);
  }
);

export default http;
