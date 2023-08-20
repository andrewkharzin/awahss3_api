// flightActions.ts
import { FlightType } from '../../../types/flight/types'
export const UPDATE_FILTERS = 'UPDATE_FILTERS';
export const SET_FLIGHTS = 'SET_FLIGHTS';

export const updateFilters = (filters: {
  iatacodeFilter: string | null;
  flightTypeFilter: string | null;
  dateFilter: string | null;
}) => {
  return {
    type: UPDATE_FILTERS,
    payload: filters,
  };
};

export const setFlights = (flights: FlightType[]) => {
  return {
    type: SET_FLIGHTS,
    payload: flights,
  };
};
