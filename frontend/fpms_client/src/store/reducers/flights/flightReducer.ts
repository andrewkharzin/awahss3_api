// flightReducer.ts
import { UPDATE_FILTERS, SET_FLIGHTS } from '../../actions/flights/flightActions';
import { FlightType } from '../../../types/flight/types'

interface FlightState {
  flights: FlightType[];
  filters: {
    iatacodeFilter: string | null;
    flightTypeFilter: string | null;
    dateFilter: string | null;
  };
}

const initialState: FlightState = {
  flights: [],
  filters: {
    iatacodeFilter: null,
    flightTypeFilter: null,
    dateFilter: null,
  },
};

const flightReducer = (state = initialState, action: any): FlightState => {
  switch (action.type) {
    case SET_FLIGHTS:
      return {
        ...state,
        flights: action.payload,
      };
    case UPDATE_FILTERS:
      return {
        ...state,
        filters: action.payload,
      };
    default:
      return state;
  }
};

export default flightReducer;
