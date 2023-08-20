import { GraphQLClient } from 'graphql-request';
import { AirlineInfo, AirlineResponse } from '../scheds/types/types'

const BASE_URL = 'http://127.0.0.1:8000/graphql'; // Замените на ваш URL GraphQL API

// Создаем GraphQL клиента
const client = new GraphQLClient(BASE_URL);



// Функция для загрузки информации о компании по коду IATA
export const fetchAirlineInfo = async (iata: string): Promise<AirlineInfo | null> => {
  const graphqlQuery = `
    query GetAirlineInfo($iata: String!) {
      airlines(codeIataAirline: $iata) {
        edges {
          node {
            nameAirline
            nameCountry
            codeHub
            arlLogo
            cntrLogo
            codeIataAirline
          }
        }
      }
    }
  `;

  try {
    const variables = { iata };
    const response = await client.request<AirlineResponse>(graphqlQuery, variables);

    if (response && response.airlines && response.airlines.edges) {
      return response.airlines.edges[0]?.node;
    } else {
      console.error('Некорректный ответ API:', response);
      return null;
    }
  } catch (error) {
    console.log('Ошибка при загрузке информации о компании:', error);
    return null;
  }
};
