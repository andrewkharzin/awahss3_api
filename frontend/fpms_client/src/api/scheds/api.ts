import axios from "axios";
import dummyFlights from "../../data/test/flights.json";

const API_KEY = "7c8a729991b6fefbfd9e89863279c947__"; // Замените на ваш ключ API

export const fetchFlights = async (page: number, query: string) => {
  try {
    const response = await axios.get(
      "http://api.aviationstack.com/v1/flights",
      {
        params: {
          access_key: API_KEY,
          limit: 100, // Максимальное количество записей
          offset: (page - 1) * 100, // Calculate the offset based on the page number
          arr_iata: "SVO",
          flight_iata: query, // Код IATA аэропорта назначения (Московский аэропорт Шереметьево)
          // flight_status: 'en-route', // Статус полета: en-route - в пути, по воздуху
        },
      }
    );

    const data = response.data;
    if (Array.isArray(data["data"])) {
      return data["data"];
    } else {
      return [];
    }
  } catch (error) {
    console.error("API Error:", error);
    return [];
  }
};

export const fetchDummyFlights = async () => {
  try {
    return dummyFlights;
  } catch (error) {
    console.log("Error fetching dummy flights:", error);
    return [];
  }
};
