export type AirlineType = {
    ageFleet: number;
    founding: number;
    sizeAirline: number;
    statusAirline: string;
    iataPrefixAccounting: number | null; // Update type to number | null
    callsign: string;
    codeHub: string;
    codeIso2Country: string;
    codeIataAirline: string;
    codeIcaoAirline: string;
    resolvedArlLogo: string;
    resolvedCntrLogo: string;
    nameAirline: string;
    nameCountry: string;
    type: string;
    // arlLogo: string;
  };
  
  export type FlightType = {
    flightNumber: string;
    airline: AirlineType;
    date: string;
    time: string;
    flightType: string;
    handlingStatus: string;
    flightRoute: string;
  };
  
  export type FlightProjectType = {
    fprjId: string;
    flight: FlightType;
    // Add other fields as needed
  };

//   const FlightsTable: React.FC = () => {
//     // ...
//   };
  