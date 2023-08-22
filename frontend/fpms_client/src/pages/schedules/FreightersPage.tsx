// ArrivalPage.tsx

import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import FreightsTable from '../../components/flights/FlightsTable'; // Assuming FlightTable.tsx is in the same directory
import { faPlaneCircleExclamation } from "@fortawesome/free-solid-svg-icons";


const ArrivalPage: React.FC = () => {
  return (
    <div>
       
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '10vh' }}>
        <span className="mx-2 mb-5 badge badge-active uppercase text-sky-400 font-bold">Arrival | <span className='text-orange-600 ml-2'>{" "}Freithters Flights</span>
        <FontAwesomeIcon
                          icon={faPlaneCircleExclamation}
                          className="text-slate-400 ml-4"
                        />
        </span>
      </div>  
      <FreightsTable />
    </div>
  );
};


export default ArrivalPage;