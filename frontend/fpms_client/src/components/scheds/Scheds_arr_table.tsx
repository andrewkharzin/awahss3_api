import React, { useState, useEffect, useCallback, useRef } from "react";
import { fetchFlights } from "../../api/scheds/api";
import { fetchAirlineInfo } from "../../api/scheds/api_graph";
// import { getAirlineLogoByIATA } from "../../api/scheds/api_graph";
import { useTheme } from "../../layouts/ThemeContext";
import "../../assets/css/flight_table.css"; // Import your CSS file
// In your main stylesheet or componen
import { Transition } from "@headlessui/react";
import { Dialog } from "@headlessui/react";
import agentsDictionary from "../../data/dicts/agents/agents";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlane } from "@fortawesome/free-solid-svg-icons";
import { Flight } from "../../api/scheds/types/types";

interface Airline {
  name: string;
  iata: string;
}

export interface AirlineInfo {
  nameAirline: string;
  nameCountry: string;
  codeHub: string;
  arlLogo: string;
  cntrLogo: string;
  codeIataAirline: string;
}

const SchedArrvTable: React.FC = () => {
  const [flights, setFlights] = useState<Flight[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedAirline, setSelectedAirline] = useState<string | null>(null);
  const [airlineOptions, setAirlineOptions] = useState<string[]>([]);
  const [sortByDate, setSortByDate] = useState<"asc" | "desc">("asc");
  const [isFiltersOpen, setIsFiltersOpen] = useState(false);
  const [airlineInfos, setAirlineInfos] = useState<AirlineInfo[]>([]);

  const toggleFilters = () => {
    setIsFiltersOpen(!isFiltersOpen);
  };

  const { darkMode } = useTheme();

  const tableClassName = `w-full table-auto ${
    darkMode
      ? "border-collapse border-slate-800 rounded-sm border-0 border-gray-800"
      : "bg-white text-black rounded-sm shadow-md"
  }`;

  // useEffect(() => {
  //   loadFlights(currentPage, searchQuery);
  // }, [currentPage, searchQuery]);

  // //Working
  // const loadFlights = async (page: number, query: string) => {
  //   try {
  //     const apiResponse = await fetchFlights(page, query);

  //     console.log("Fetched flights data:", apiResponse);
  //     setFlights(apiResponse); // No need for "data as Flight[]"
  //   } catch (error) {
  //     console.log(error);
  //   }

  // };

  // Experimental
  useEffect(() => {
    const loadFlights = async (page: number, query: string) => {
      try {
        const flightsData = await fetchFlights(page, query);
        setFlights(flightsData);

        // Fetch airline information
        const airlineInfos = await Promise.all(
          flightsData.map(async (flight: Flight) => {
            return await fetchAirlineInfo(flight.airline.iata);
          })
        );

        // Очищаем массив от null значений
        const validAirlineInfos = airlineInfos.filter(
          (info): info is AirlineInfo => info !== null
        );

        // Применяем validAirlineInfos к setAirlineInfos
        setAirlineInfos(validAirlineInfos);
      } catch (error) {
        console.log(error);
      }
    };

    loadFlights(1, ""); // Load flights on component mount
  }, []);

  const handleNextPage = () => {
    setCurrentPage((prevPage) => prevPage + 1);
  };

  const handlePrevPage = () => {
    setCurrentPage((prevPage) => prevPage - 1);
  };

  useEffect(() => {
    const uniqueAirlines: string[] = Array.from(
      new Set(flights.map((flight: Flight) => flight.airline.iata))
    );
    setAirlineOptions(uniqueAirlines);
  }, [flights]);

  const handleAirlineChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedAirline(event.target.value);
  };

  const handleSortByDate = () => {
    setSortByDate(sortByDate === "asc" ? "desc" : "asc");
  };

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(event.target.value);
  };

  // const filteredFlights = selectedAirline
  //   ? flights.filter((flight: Flight) => flight.airline.iata === selectedAirline)
  //   : flights;

  const filteredFlights = flights.filter((flight) =>
    selectedAirline ? flight.airline.iata === selectedAirline : true
  );

  filteredFlights.sort((a, b) => {
    const dateA = new Date(a.flight_date).getTime();
    const dateB = new Date(b.flight_date).getTime();

    return sortByDate === "asc" ? dateA - dateB : dateB - dateA;
  });

  const formatDateTime = (dateTimeStr: string) => {
    const options: Intl.DateTimeFormatOptions = {
      day: "numeric",
      month: "numeric",
      hour: "numeric",
      minute: "numeric",
      hour12: false,
      timeZone: "UTC",
    };
    return new Date(dateTimeStr).toLocaleString("en-US", options);
  };
  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    const month = (date.getMonth() + 1).toString().padStart(2, "0"); // Add 1 to month index since it's 0-based
    const day = date.getDate().toString().padStart(2, "0");
    return `${month}/${day}`;
  };

  const calculateFlightTime = (
    departureTime: string,
    arrivalTime: string
  ): string => {
    const departure = new Date(departureTime);
    const arrival = new Date(arrivalTime);
    const diffInMinutes =
      Math.abs(arrival.getTime() - departure.getTime()) / 60000; // Convert milliseconds to minutes

    const hours = Math.floor(diffInMinutes / 60);
    const minutes = Math.floor(diffInMinutes % 60);

    return `${hours}:${minutes.toString().padStart(2, "0")}`;
  };

  return (
    <div className="relative">
      <div className="flext py-5 space-x-2">
        <button
          className="btn btn-sm px-4 py-2 rounded focus:outline-none"
          onClick={toggleFilters}
        >
          Filters
        </button>
        <button
          className="btn btn-sm mr-2"
          disabled={currentPage === 1}
          onClick={handlePrevPage}
        >
          Previous Page
        </button>
        <button className="btn btn-sm" onClick={handleNextPage}>
          Next Page
        </button>
        <input
          type="text"
          value={searchQuery}
          onChange={handleSearchChange}
          placeholder="Search by flight number"
          className="input input-bordered w-full max-w-xs"
        />
      </div>
      <Dialog open={isFiltersOpen} onClose={() => setIsFiltersOpen(false)}>
        <div className="fixed inset-0 flex justify-center items-center z-10">
          <Dialog.Overlay className="fixed inset-0 bg-black opacity-30" />

          <div className="bg-gray-800 w-[800px] top-20 p-4 rounded shadow-md z-20">
            <div className="md:flex md:items-center md:space-x-4 md:space-y-0">
              <div>
                <label className="label">
                  <span className="label-text">Sort date by asc/desc</span>
                </label>
                <button onClick={handleSortByDate} className="btn btn-neutral">
                  {sortByDate === "asc" ? "Sort >" : "Sort <"}
                </button>
              </div>

              <div>
                <label htmlFor="airlineSelect" className="label">
                  <span className="label-text">Choose Airline</span>
                </label>
                <select
                  className="select w-full max-w-xs"
                  value={selectedAirline || ""}
                  onChange={handleAirlineChange}
                >
                  <option disabled selected>
                    Pick Airline
                  </option>
                  <option value="">All Airlines</option>
                  {airlineOptions.map((iata) => (
                    <option key={iata} value={iata}>
                      {iata}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <button onClick={() => setIsFiltersOpen(false)}>Close</button>
          </div>
        </div>
      </Dialog>

      <div className="w-full overflow-x-auto">
        <table className="w-full table-auto table-zebra">
          <thead>
            <tr>
              <th className="p-2 text-left font-normal min-w text-sm uppercase">
                Flight Date
              </th>
              <th className="p-2 text-left text-sm uppercase">Airline</th>
              <th className="p-2 text-left text-sm uppercase">HStates</th>
              <th className="p-2 text-left min-w text-sm uppercase">Number</th>
              <th className="p-2 text-left min-w text-sm uppercase">From</th>
              <th className="p-2 text-left text-sm uppercase">To</th>
              <th className="p-2 text-left min-w">Dep Airport times</th>
              <th className="p-2 text-left text-sm uppercase">Arr SVO times</th>
              <th className="p-2 text-left text-sm uppercase">TFE</th>
            </tr>
          </thead>
          <tbody>
            {filteredFlights.map((flight: any, index: number) => (
              <tr key={index}>
                <td className="px-2 py-2">{formatDate(flight.flight_date)}</td>
                <td>
                  <div className="flex items-center space-x-3">
                    <div className="avatar">
                    {airlineInfos[index]?.arlLogo && (
                      <div className="w-8 rounded">
                        <img
                          src={airlineInfos[index]?.arlLogo}
                          alt={flight.airline.callsign}
                        />
                      </div>
                    )}
                    </div>
                    <div>
                      <div className="font-bold">{flight.airline.name}</div>
                      <div className="text-sm opacity-50">ecec</div>
                    </div>
                  </div>
                </td>
                <td className="p-2 py-2">
                  <h5 className="text-sm font-light">
                    GHA:
                    <span
                      className={`badge badge-xs font-bold ${agentsDictionary[flight.airline.iata] === "AGK"
                          ? "text-red-500"
                          : "text-sky-400"
                        }`}
                    >
                      {agentsDictionary[flight.airline.iata] || "-"}
                    </span>
                  </h5>

                  <h5 className="text-xs uppercase text-slate-500">
                    {flight.flight_status === "active" ? (
                      <span className="text-sky-600 font-bold">
                        OnFly
                        <FontAwesomeIcon
                          icon={faPlane}
                          size="xs"
                          className="ml-2 fly-blink-icon text-sky-300"
                        />
                      </span>
                    ) : flight.flight_status === "landed" ? (
                      <span className="text-green-700 font-bold">
                        OnGround
                        <FontAwesomeIcon
                          icon={faPlane}
                          size="xs"
                          className="ml-2 text-green-400"
                        />
                      </span>
                    ) : (
                      <span className="font-bold">
                        {flight.flight_status}
                        <FontAwesomeIcon
                          icon={faPlane}
                          size="xs"
                          className="ml-2 text-gray-400"
                        />
                      </span>
                    )}
                  </h5>
                </td>

                <td className="p-2 py-2 text-left font-normal text-slate-600">
                  <div className="flex items-center">
                    <span className="text-xs text-gray-500">
                      <p className="py-1 ext-xs font-bold">
                        IATA:
                        <span className="badge text-sky-600 rounded-l-sm badge-sm">
                          {" "}
                          {flight.flight.iata}
                        </span>
                      </p>
                    </span>
                  </div>
                  <span className="text-xs text-gray-500">
                    <p className="py-1 border-slate-700 font-light">
                      IACO:
                      <span className="badge rounded-l-sm badge-sm">
                        {" "}
                        {flight.flight.icao}
                      </span>
                    </p>
                  </span>
                </td>

                <td className="font-bold text-orange-500">
                  <button className="btn btn-sm btn-active text-orange-500">
                    {flight.departure.iata}
                  </button>
                </td>
                <td className="font-bold text-slate-500">
                  {flight.arrival.iata}
                </td>
                <td className="p-2 text-left font-normal text-slate-600">
                  <div className="flex items-center">
                    <span className="text-xs text-gray-500">
                      <p className="py-1 border-slate-300 ext-xs font-bold">
                        STD:
                        <span className="badge rounded-l-sm badge-sm">
                          {" "}
                          {formatDateTime(flight.departure.scheduled)}
                        </span>
                      </p>
                    </span>
                  </div>
                  <span className="text-xs text-gray-500">
                    <p className="py-1  border-slate-600 font-bold">
                      ETD:
                      <span className="badge rounded-l-sm badge-sm">
                        {" "}
                        {formatDateTime(flight.departure.estimated)}
                      </span>
                    </p>
                  </span>
                </td>
                <td className="p-2 text-left font-normal text-slate-600">
                  <div className="flex items-center">
                    <span className="text-xs text-gray-500">
                      <p className="py-1 border-slate-300 ext-xs font-bold">
                        STA:
                        <span className="badge rounded-l-sm text-green-600 badge-sm">
                          {" "}
                          {formatDateTime(flight.arrival.scheduled)}
                        </span>
                      </p>
                    </span>
                  </div>
                  <span className="text-xs text-gray-500">
                    <p className="py-1 border-t border-slate-600 font-bold">
                      ETA:
                      <span className="badge rounded-l-sm text-orange-600 badge-sm">
                        {" "}
                        {formatDateTime(flight.arrival.estimated)}
                      </span>
                    </p>
                  </span>
                </td>
                <td className="p-2 text-left font-normal text-slate-600">
                  <div className="flex items-center">
                    <span className="text-xs text-gray-500">
                      <p className="py-1 border-slate-300 ext-xs font-bold">
                        SFT:
                        <span className="badge rounded-l-sm text-gray-300 badge-sm">
                          {" "}
                          {calculateFlightTime(
                            flight.departure.scheduled,
                            flight.arrival.scheduled
                          )}
                        </span>
                      </p>
                    </span>
                  </div>
                  <span className="text-xs text-gray-500">
                    <p className="py-1 border-t border-slate-600 font-bold">
                      EFT:
                      <span className="badge rounded-l-sm text-gray-400 badge-sm">
                        {" "}
                        {calculateFlightTime(
                          flight.departure.estimated,
                          flight.arrival.estimated
                        )}
                      </span>
                    </p>
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default SchedArrvTable;
