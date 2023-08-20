import React, { useState, useEffect, useMemo } from "react";
import { useTheme } from "../../layouts/ThemeContext";
import { FlightType } from "../../types/flight/types";
import { getAllFlights } from "../../api/api"; // Import the specific function
import "../../assets/css/flight_table.css"; // Import your CSS file
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faPlaneArrival,
  faPlaneDeparture,
} from "@fortawesome/free-solid-svg-icons";
import FlightTableSkeleton from "./FlightTableSkeleton";
// import FlightDetailModal from "./modals/FlightDetailModal";
import {
  faClock,
  faCheckCircle,
  faTimesCircle,
  faBan,
} from "@fortawesome/free-solid-svg-icons";
import { useDispatch, useSelector } from "react-redux";
import { updateFilters } from "../../store/reducers/flights/actions";
import Modal from "../flights/modals/modal";

const filterFlights = (
  flight: FlightType,
  iataFilter: string | null,
  flightTypeFilter: string | null,
  dateFilter: string | null,
  handlingFilter: string | null
) => {
  return (
    (iataFilter === null ||
      flight.airline.codeIataAirline.toLowerCase() ===
        iataFilter.toLowerCase()) &&
    (flightTypeFilter === null || flight.flightType === flightTypeFilter) &&
    (dateFilter === null || flight.date === dateFilter) &&
    (handlingFilter === null || flight.handlingStatus === handlingFilter)
  );
};

const FlightsTable: React.FC = () => {
  const dispatch = useDispatch();

  const filters = useSelector((state: any) => state.filters);

  const updateFilter = (name: string, value: string | null) => {
    const updatedFilters = { ...filters, [name]: value };
    dispatch(updateFilters(updatedFilters));
  };

  const clearFilters = () => {
    setIatacodeFilter(null);
    setFlightTypeFilter(null);
    setDateFilter(null);
    setHandlingFilter(null);
  };

  const { darkMode } = useTheme();

  const tableClassName = `w-full table-auto ${
    darkMode
      ? "border-collapse border-slate-800 rounded-sm border-0 border-gray-800"
      : "bg-white text-black rounded-sm shadow-md"
  }`;
  const BASE_URL = "http://127.0.0.1:8000";
  const [flights, setFlights] = useState<FlightType[]>([]);
  const [displayInUTC, setDisplayInUTC] = useState(false);
  const [iatacodeFilter, setIatacodeFilter] = useState<string | null>(null);
  const [flightTypeFilter, setFlightTypeFilter] = useState<string | null>(null);
  const [handlingTypeFilter, setHandlingFilter] = useState<string | null>(null);
  const [dateFilter, setDateFilter] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [selectedFlight, setSelectedFlight] = useState<FlightType | null>(null);

  const [open, setOpen] = useState(false);
  const handleToggle = () => setOpen((prev) => !prev);

  const formatTime = (time: string) => {
    const [hours, minutes] = time.split(":");
    return `${hours}:${minutes}`;
  };

  const formatDateAndTime = (date: string, time: string, useUTC: boolean) => {
    const dateTime = new Date(`${date}T${time}`);
    const formattedTime = useUTC
      ? formatTime(time)
      : dateTime.toLocaleTimeString("en-US", {
          hour: "numeric",
          minute: "numeric",
          hour12: false,
        });

    if (useUTC) {
      const formattedUTCDate = dateTime.toISOString().split("T")[0];
      return `${formattedUTCDate} ${formattedTime} (UTC)`;
    } else {
      const formattedDate = dateTime.toLocaleDateString("en-GB", {
        day: "numeric",
        month: "numeric",
        year: "numeric",
      });
      return `${formattedDate} ${formattedTime}`;
    }
  };

  const [sortAscending, setSortAscending] = useState(true);

  const toggleSortOrder = () => {
    setSortAscending((prevSortOrder) => !prevSortOrder);
  };

  const toggleDisplayMode = () => {
    setDisplayInUTC(!displayInUTC);
  };

  const sortedFlights = useMemo(() => {
    const filtered = flights.filter((flight) =>
      filterFlights(
        flight,
        iatacodeFilter,
        flightTypeFilter,
        dateFilter,
        handlingTypeFilter
      )
    );

    const sorted = filtered.sort((a, b) => {
      const dateA = new Date(a.date).getTime();
      const dateB = new Date(b.date).getTime();

      return sortAscending ? dateA - dateB : dateB - dateA;
    });

    return sorted;
  }, [
    flights,
    iatacodeFilter,
    flightTypeFilter,
    dateFilter,
    handlingTypeFilter,
    sortAscending,
  ]);

  const openFlightDetailModal = (flight: FlightType) => {
    setSelectedFlight(flight);
    console.log("Selected flight:", selectedFlight);
    console.log("Modal opened for flight:", flight);
  };

  const closeFlightDetailModal = () => {
    setSelectedFlight(null);
  };

  useEffect(() => {
    // Fetch flights using the API function
    getAllFlights()
      .then((response) => {
        setFlights(response);
        setLoading(false); //
        console.log("Flights data:", response);
      })
      .catch((error) => {
        console.error("Error fetching flights:", error);
        setFlights([]); // Handle error by setting an empty array or other appropriate value
      });
  }, []);

  useEffect(() => {
    console.log("Selected flight (inside useEffect):", selectedFlight);
  }, [selectedFlight]);

  return (
    <div className="w-full overflow-x-auto">
      {/* <FlightTableSkeleton /> */}
      <div className="py-10 md:flex md:items-center md:space-x-4 md:space-y-0">
        <button onClick={toggleDisplayMode} className="btn btn-neutral">
          {displayInUTC ? "Local" : "UTC"}
        </button>
        <button onClick={clearFilters} className="btn btn-neutral">
          Clear
        </button>
        <button onClick={toggleSortOrder} className="btn btn-neutral">
          {sortAscending ? "Sort Descending" : "Sort Ascending"}
        </button>

        <input
          type="text"
          placeholder="Filter by IATA Code"
          value={iatacodeFilter || ""}
          onChange={(e) => setIatacodeFilter(e.target.value)}
          className="uppercase input input-ghost max-w-xs w-full md:max-w-sm"
        />
        <select
          className="select max-w-xs w-full md:max-w-sm"
          value={flightTypeFilter || ""}
          onChange={(e) => setFlightTypeFilter(e.target.value)}
        >
          <option value="">All Flight Types</option>
          <option value="departure">Departure</option>
          <option value="arrival">Arrival</option>
        </select>
        <select
          className="select max-w-xs w-full md:max-w-sm"
          value={handlingTypeFilter || ""}
          onChange={(e) => setHandlingFilter(e.target.value)}
        >
          <option value="">All Handling Status</option>
          <option value="New">New</option>
          <option value="StandBy">StandBy</option>
          <option value="Completed">Completed</option>
          <option value="Rejected">Rejected</option>
          <option value="Canceled">Canceled</option>
          {/* Add more options if needed */}
        </select>
      </div>
      <div className="w-full overflow-x-auto py-5 mx-2">
        {loading ? (
          <FlightTableSkeleton /> // Display skeleton loading while data is loading
        ) : (
          <table className="w-full table-auto table-zebra">
            <thead>
              <tr>
                <th className="p-2 text-left text-sm uppercase">Airline</th>
                {/* <th className="p-2 text-left text-sm uppercase">Stats</th> */}
                <th className="p-2 text-left text-sm uppercase">
                  Flight number
                </th>
                <th className="p-2 text-left text-sm uppercase">Route</th>
                <th className="p-2 text-left text-sm uppercase">
                  <div
                    className="tooltip"
                    data-tip="Planning Flight Time and Date"
                  >
                    <button className="btn btn-sm">PFT</button>
                  </div>
                </th>
                <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Arrival or Departure">
                    <button className="btn btn-sm">Type</button>
                  </div>
                </th>
                <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Handling status">
                    <button className="btn btn-sm">Status</button>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>
              {sortedFlights.map((flight) => (
                <tr
                  key={flight.flightNumber}
                  className="hover:bg-slate-700 border-b border-slate-700"
                >
                  <td className="px-2 py-2">
                    <div className="flex items-center space-x-3">
                      <div className="avatar">
                        <div className="w-8 rounded">
                          <img
                            src={`${BASE_URL}${flight.airline.resolvedArlLogo}`}
                            alt={flight.airline.callsign}
                          />
                        </div>
                      </div>
                      <div>
                        <div className="font-bold text-orange-500">
                          {flight.airline.callsign}
                        </div>
                        <div className="font-extralight text-slate-500">
                          {flight.airline.nameAirline}
                        </div>
                      </div>
                    </div>
                  </td>
                  {/* <td className="px-2 text-left">
                    <h5 className="text-sm">
                      AWB
                      <span className="badge badge-xs text-purple-600 font-bold">
                        {flight.airline.iataPrefixAccounting !== null
                          ? flight.airline.iataPrefixAccounting
                          : "NIL"}
                      </span>
                    </h5>
                  </td> */}
                  <td className="px-2 text-left">
                    <div className="flex items-center space-x-3">
                      <div className="avatar">
                        <div className="w-4">
                          <img
                            src={`${BASE_URL}${flight.airline.resolvedCntrLogo}`}
                            alt={flight.airline.callsign}
                          />
                        </div>
                      </div>
                      {/* <button
                        className="btn btn-sm"
                        onClick={() => openFlightDetailModal(flight)}
                      >
                        {flight.airline.codeIataAirline}
                        <div className="badge rounded-l text-orange-600">
                          {flight.flightNumber}
                        </div>
                      </button> */}
                      <button
                        className="btn btn-sm"
                        onClick={() => openFlightDetailModal(flight)}
                      >
                        {flight.airline.codeIataAirline ? (
                          <>
                            {flight.airline.codeIataAirline}
                            <div className="badge rounded-l text-orange-600">
                              {flight.flightNumber}
                            </div>
                          </>
                        ) : (
                          <>
                            {flight.airline.codeIcaoAirline}
                            <div className="badge rounded-l text-green-600">
                              {flight.flightNumber}
                            </div>
                          </>
                        )}
                      </button>
                    </div>
                  </td>
                  <td className="p-2 text-left">
                    {flight.flightType === "departure" ? (
                      <>
                        <span className="font-bold text-slate-500">SVO</span>
                        <FontAwesomeIcon
                          icon={faPlaneDeparture}
                          size="sm"
                          className="px-1 text-slate-500"
                        />
                        <span className="font-bold text-orange-500">
                          {flight.flightRoute}
                        </span>
                      </>
                    ) : (
                      <>
                        <span className="font-bold text-orange-500">
                          {flight.flightRoute}
                        </span>
                        <FontAwesomeIcon
                          icon={faPlaneArrival}
                          size="sm"
                          className="px-1 text-slate-500"
                        />
                        <span className="font-bold text-slate-500">SVO</span>
                      </>
                    )}
                  </td>
                  <td className="p-2 text-left font-normal text-slate-500">
                    <div className="flex items-center">
                      <FontAwesomeIcon
                        icon={faClock}
                        className="mr-2 text-slate-500"
                      />
                      {formatDateAndTime(
                        flight.date,
                        flight.time,
                        displayInUTC
                      )}
                    </div>
                  </td>
                  <td className="p-2 text-left">
                    <span className="font-bold uppercase text-slate-500">
                      {flight.flightType}
                    </span>
                  </td>
                  <td className="p-2">
                    {flight.handlingStatus === "New" ? (
                      <span className="flex items-center">
                        <FontAwesomeIcon
                          icon={faCheckCircle}
                          className="text-orange-500 mr-1"
                        />
                        <span className="font-bold uppercase text-base text-orange-500">
                          {flight.handlingStatus}
                        </span>
                      </span>
                    ) : flight.handlingStatus === "StandBy" ? (
                      <span className="flex items-center">
                        <FontAwesomeIcon
                          icon={faClock}
                          className="text-green-600 mr-1"
                        />
                        <span className="font-bold uppercase text-base text-green-600">
                          {flight.handlingStatus}
                        </span>
                      </span>
                    ) : flight.handlingStatus === "Rejected" ? (
                      <span className="flex items-center">
                        <FontAwesomeIcon
                          icon={faTimesCircle}
                          className="text-red-600 mr-1"
                        />
                        <span className="font-bold uppercase text-base text-red-600">
                          {flight.handlingStatus}
                        </span>
                      </span>
                    ) : flight.handlingStatus === "Canceled" ? (
                      <span className="flex items-center">
                        <FontAwesomeIcon
                          icon={faBan}
                          className="text-gray-600 mr-1"
                        />
                        <span className="font-bold uppercase text-base text-gray-600">
                          {flight.handlingStatus}
                        </span>
                      </span>
                    ) : (
                      flight.handlingStatus
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
        {/* <Modal open={selectedFlight !== null} flight={selectedFlight!} onClose={closeFlightDetailModal} /> */}
        <Modal
          open={selectedFlight !== null}
          flight={selectedFlight!}
          onClose={closeFlightDetailModal}
        >
          {selectedFlight && (
            <>
              <div className="banner h-200 bg-base-100 flex items-left justify-center sm:w-full">
                <div className="banner overflow-hidden h-[15vw] w-full">
                  <img
                    src="https://images6.alphacoders.com/569/thumbbig-569032.webp"
                    alt="Banner Image"
                    className="rounded-tl-3xl object-cover w-full h-full"
                  ></img>
                </div>
              </div>
              <div className="card mx-2">
                <h2 className="card-title ml-5 mt-5">
                  <span className="btn btn-active btn-sm font-bold text-orange-600">
                    {selectedFlight.airline.codeIataAirline}
                  </span>
                  {selectedFlight.flightNumber}
                  {" | "}
                  {selectedFlight.airline.callsign}
                  <div className="avatar">
                    <div className="w-4 text-sm">
                      <img
                        src={`${BASE_URL}${selectedFlight.airline.resolvedCntrLogo}`}
                        alt={selectedFlight.airline.callsign}
                      />
                    </div>
                  </div>
                  <div className="flex text-sm items-center">
                    <FontAwesomeIcon
                      icon={faClock}
                      className="ml-5 text-sky-500"
                    />
                    <span className="ml-5 ">
                      {formatDateAndTime(
                        selectedFlight.date,
                        selectedFlight.time,
                        displayInUTC
                      )}
                    </span>
                    {"  "}
                    <span className="badget badget-ghost ml-5 font-bold text-slate-500 text-sm  uppercase">
                      MVT:NIL
                    </span>
                  </div>
                </h2>
                <div className="divider"></div>
              </div>

              {/* Add more flight details here */}
              <div className="modal-action">
                <button
                  className="btn btn-active rounded-br-3xl mb-2 mx-2"
                  onClick={closeFlightDetailModal}
                >
                  Close
                </button>
              </div>
            </>
          )}
        </Modal>
      </div>
    </div>
  );
};

export default FlightsTable;
