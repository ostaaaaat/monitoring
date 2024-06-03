import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // Адрес вашего FastAPI сервера
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default {
  uploadCsv(file) {
    let formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  },
  getGraphs(parametr, date_from, date_to, grouping) {
    return apiClient.get('/graphs', {
      params: {
        parametr,
        date_from,
        date_to,
        grouping
      }
    });
  },
  getDiagrams(parametr, date_from, date_to) {
    return apiClient.get('/diagrams', {
      params: {
        parametr,
        date_from,
        date_to
      }
    });
  },
  getHeatmaps(parametr, lat_min, lat_max, lon_min, lon_max) {
    return apiClient.get('/heatmaps', {
      params: {
        parametr,
        lat_min,
        lat_max,
        lon_min,
        lon_max
      }
    });
  },
};
