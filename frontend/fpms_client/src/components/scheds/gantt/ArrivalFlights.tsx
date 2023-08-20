import React from 'react';
// import 'mermaid/dist/mermaid.css';
import mermaid from 'mermaid';
import { Flight } from '../../../api/scheds/types/types'; // Укажите правильный путь к файлу

// Initialize Mermaid
mermaid.initialize({
  startOnLoad: true,
});

const FlightGanttChart = ({ flights }: { flights: Flight[] }) => {
  const ganttChartDefinition = `
    gantt
      title Flight Schedule
      dateFormat YYYY-MM-DD HH:mm:ss

      section Flights
      ${flights
        .map(
          (flight, index) => `
        ${index + 1}. ${flight.flight.number} : ${flight.departure.scheduled} - ${flight.arrival.scheduled}
        `
        )
        .join('\n')}
    `;

  return <div className="mermaid">{ganttChartDefinition}</div>;
};

export default FlightGanttChart;
