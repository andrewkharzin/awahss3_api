import axios from 'axios';

export interface Flight {
  flight_date: string;
  flight_status: string;
  departure: {
    airport: string;
    timezone: string | null;
    iata: string;
    icao: string;
    terminal: string | null;
    gate: string | null;
    delay: number | null;
    scheduled: string;
    estimated: string;
    actual: string | null;
    estimated_runway: string | null;
    actual_runway: string | null;
  };
  arrival: {
    airport: string;
    timezone: string;
    iata: string;
    icao: string;
    terminal: string | null;
    gate: string | null;
    baggage: string | null;
    delay: number | null;
    scheduled: string;
    estimated: string;
    actual: string | null;
    estimated_runway: string | null;
    actual_runway: string | null;
  };
  airline: {
    name: string;
    iata: string;
    icao: string;
  };
  flight: {
    number: string;
    iata: string;
    icao: string;
    codeshared: any;
  };
  aircraft: any;
  live: any;
}


export interface Airline { 
    name: string;
    iata: string;
    icao: string;
}


export interface AirlineInfo {
  nameAirline: string;
  nameCountry: string;
  codeHub: string;
  arlLogo: string;
  cntrLogo: string;
  codeIataAirline: string;
}

export interface AirlineResponse {
  airlines: {
    edges: {
      node: AirlineInfo;
    }[];
  };
}