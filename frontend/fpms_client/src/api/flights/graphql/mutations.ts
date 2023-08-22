import { gql } from '@apollo/client';

export const CREATE_FLIGHT_MUTATION = gql`
  mutation CreateFlight(
    $airlineIatacode: String!
    $flightType: String!
    $handlingStatus: String!
    $date: String!
  ) {
    createFlight(
      airlineIatacode: $airlineIatacode
      flightType: $flightType
      handlingStatus: $handlingStatus
      date: $date
    ) {
      flightType
      flightNumber
      flightRoute
      handlingStatus
      time
      date
    }
  }
`;
