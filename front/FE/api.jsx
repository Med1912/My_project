import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json", 
  },
});


export const getAssociations = () => API.get("/associations/");
export const getDemandes = () => API.get("/demandes/");
export const engagerTache = (demandeId) => API.post(`/taches/engager/${demandeId}`);
export const getMesTaches = () => API.get("/taches/mes-taches");

export default API;

