import React, { useState } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import AddFlight from '../../components/flights/AddFlight';
import { faPlaneArrival } from "@fortawesome/free-solid-svg-icons";
import { FlightType } from '../../types/flight/types';

const CreateFreightPage: React.FC = () => {
  const handleFlightAdded = (flight: FlightType) => {
    // Handle the flight added event, if needed
    console.log('New flight added:', flight);
  };

  return (
    <div>
      <span className="mx-2 mb-5 badge badge-active uppercase text-sky-400 font-bold">
        Arrival  <span className='text-orange-600'>Freighters Flights</span>
        <FontAwesomeIcon
          icon={faPlaneArrival}
          size="lg"
          className="ml-2 text-gray-400/50"
        />
      </span>

      {/* Pass the onFlightAdded prop */}
      <AddFlight onFlightAdded={handleFlightAdded} />

    </div>
  );
};

export default CreateFreightPage;
