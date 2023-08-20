import axios from 'axios';
import { GET_ALL_FLIGHTS, GET_ALL_FLIGHT_PROJECTS } from './flights/query';

const API_URL = process.env.REACT_APP_API_URL;

export const getAllFlights = async () => {
  try {
    const response = await axios.post(API_URL!, {
      query: GET_ALL_FLIGHTS,
    });
    return response.data.data.allFlights;
  } catch (error) {
    console.error('Error fetching flights:', error);
    return [];
  }
};

export const getAllFlightProjects = async () => {
  try {
    const response = await axios.post(API_URL!, {
      query: GET_ALL_FLIGHT_PROJECTS,
    });
    return response.data.data.allFlightProjects;
  } catch (error) {
    console.error('Error fetching flight projects:', error);
    return [];
  }
};
