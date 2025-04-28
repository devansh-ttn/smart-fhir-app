import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE
});

export default {
  getPatientInfo: async () => {
    const response = await api.get('/fhir/Patient');
    return response.data;
  }
};