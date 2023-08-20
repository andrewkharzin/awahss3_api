import React, { useEffect, useState } from 'react';
import { getAllFlights, getAllFlightProjects } from '../../api/api';
import { FlightType, FlightProjectType } from '../../types/flight/types'; // Define your types

const FlightList: React.FC = () => {
  const [flights, setFlights] = useState<FlightType[]>([]);

  useEffect(() => {
    const fetchFlights = async () => {
      const fetchedFlights = await getAllFlights();
      console.log('Fetched flights:', fetchedFlights); // Log the fetched flights
      setFlights(fetchedFlights);
    };

    fetchFlights();
  }, []);

  return (
    <div>
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-slate-800 text-xs font-normal text-orange-200">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Flight Number
            </th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Airline
            </th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Date
            </th>
            {/* Add more columns here */}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {flights.map((flight) => (
            <tr key={flight.flightNumber}>
              <td className="px-6 py-4 whitespace-nowrap">{flight.flightNumber}</td>
              <td className="px-6 py-4 whitespace-nowrap">{flight.airline.codeIataAirline}</td>
              <td className="px-6 py-4 whitespace-nowrap">{flight.date}</td>
              {/* Add more columns here */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const ProjectList: React.FC = () => {
  const [flightProjects, setFlightProjects] = useState<FlightProjectType[]>([]);

  useEffect(() => {
    const fetchFlightProjects = async () => {
      const fetchedProjects = await getAllFlightProjects();
      console.log('Fetched flight projects:', fetchedProjects); // Log the fetched projects
      setFlightProjects(fetchedProjects);
    };

    fetchFlightProjects();
  }, []);

  return (
    <div>
    <table className="min-w-full divide-y divide-slate-800">
      <thead className="bg-slate-800">
        <tr>
          <th className="px-6 py-3 text-left font-mono text-sm text-thin text-orange-500 uppercase tracking-wider">
            Custom ID
          </th>
          <th className="px-6 py-3 text-left font-mono text-sm text-thin text-orange-500 uppercase tracking-wider">
            Flight Number
          </th>
          {/* Add more columns here */}
        </tr>
      </thead>
      <tbody className="bg-white divide-y divide-slate-700">
        {flightProjects.map((project) => (
          <tr key={project.fprjId}>
            <td className="px-6 py-4 text-cyan-800 whitespace-nowrap">{project.fprjId}</td>
            <td className="px-6 py-4 whitespace-nowrap">
              {project.flight.flightNumber} - {project.flight.airline.codeIataAirline}
            </td>
            {/* Add more columns here */}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  );
};

export { FlightList, ProjectList };
