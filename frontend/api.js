import axios from 'axios';

export const predict = (data) => {
  return axios.post('http://localhost:5000/api/predict', data);
};
