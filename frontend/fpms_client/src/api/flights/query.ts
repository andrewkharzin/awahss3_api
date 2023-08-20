const GET_ALL_FLIGHTS = `
  query {
    allFlights {
      airline {
        nameAirline
        ageFleet
        bannerImg
        callsign
        codeHub
        codeIataAirline
        codeIcaoAirline
        codeIso2Country
        founding
        iataPrefixAccounting
        nameCountry
        resolvedArlLogo
        sizeAirline
        statusAirline
        type
        resolvedArlLogo
        resolvedCntrLogo
      }
      date
      flightType
      flightNumber
      time
      handlingStatus
      flightRoute
    }
  }
`;

const GET_ALL_FLIGHT_PROJECTS = `
  query {
    allFlightProjects {
      fprjId
      flight {
        flightNumber
        airline {
          codeIataAirline
        }
        date
        time
        flightType
      }
    }
  }
`;

export { GET_ALL_FLIGHTS, GET_ALL_FLIGHT_PROJECTS };
