// ArrivalPage.tsx

import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import FlightTable from '../../components/scheds/Scheds_arr_table'; // Assuming FlightTable.tsx is in the same directory
import { faPlaneArrival } from "@fortawesome/free-solid-svg-icons";

const ArrivalPage: React.FC = () => {
  return (
    <div>
      <span className="mx-5 badge badge-active uppercase text-sky-400 font-bold">Arrival<span className='text-orange-600'> Flights</span>
      <FontAwesomeIcon
                          icon={faPlaneArrival}
                          size="lg"
                          className="ml-2 text-gray-400/50"
                        />
      </span>
      <FlightTable />
    </div>
  );
};


export default ArrivalPage;