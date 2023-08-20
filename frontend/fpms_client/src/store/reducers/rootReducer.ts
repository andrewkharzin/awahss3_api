import { combineReducers } from 'redux';
import flightReducer from '../reducers/flights/flightReducer';

const rootReducer = combineReducers({
  flight: flightReducer,
  // Add other reducers here if needed
});

export default rootReducer;