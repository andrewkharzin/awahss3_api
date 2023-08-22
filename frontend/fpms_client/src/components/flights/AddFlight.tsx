import React, { useState } from 'react';
import { useMutation } from '@apollo/client';
import { CREATE_FLIGHT_MUTATION } from '../../api/flights/graphql/mutations';
import { FlightType } from '../../types/flight/types';

interface AddFlightProps {
  onFlightAdded: (flight: FlightType) => void;
}

const AddFlight: React.FC<AddFlightProps> = ({ onFlightAdded }) => {
  const [airlineIatacode, setAirlineIatacode] = useState('');
  const [flightType, setFlightType] = useState('');
  const [handlingStatus, setHandlingStatus] = useState('');
  const [date, setDate] = useState('');
  const [createFlight, { loading, error }] = useMutation(CREATE_FLIGHT_MUTATION);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await createFlight({
        variables: {
          airlineIatacode,
          flightType,
          handlingStatus,
          date,
        },
      });

      const newFlight = response.data.createFlight;

      onFlightAdded(newFlight);

      setAirlineIatacode('');
      setFlightType('');
      setHandlingStatus('');
      setDate('');
    } catch (error) {
      console.error('Error creating flight:', error);
    }
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <h2>Add New Flight</h2>
      <form onSubmit={handleSubmit}>
        {/* Input fields for airlineIatacode, flightType, handlingStatus, date */}
        <button type="submit">Add Flight</button>
      </form>
    </div>
  );
};

export default AddFlight;
