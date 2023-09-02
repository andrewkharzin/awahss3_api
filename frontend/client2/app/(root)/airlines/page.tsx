
import { SearchInput } from '@/components/search-input';
import { getClient } from "@/lib/client";
import { gql } from "@apollo/client";

type Airline = {
	codeIataAirline: string;
	resolvedArlLogo: string;
	iataPrefixAccounting: string;
	nameAirline: string;
	nameCountry: string;
	type: string;
	statusAirline: string;
	resolvedCntrLogo: string;
	codeIso2Country: string;
	codeIcaoAirline: string;
	callsign: string;
	bannerImg: string;
	codeHub: string;
	// Add other fields if needed
  };

const query = gql`
  query Now {
    airlines {
      codeIataAirline
      resolvedArlLogo
      iataPrefixAccounting
      nameAirline
      nameCountry
      type
      statusAirline
      resolvedCntrLogo
      codeIso2Country
      codeIcaoAirline
      callsign
      bannerImg
      codeHub
    }
  }
`;

type AirlinesProps = {
	airlines: Airline[];
  };

export default function Airlines({ airlines }: AirlinesProps) {
  console.log("Fetched airlines data:", airlines);
  return (
    <main>
      <h1>Airlines</h1>
      <ul>
        {airlines.map((airline) => (
          <li key={airline.codeIataAirline}>
            {airline.nameAirline}
            {/* Render other airline data */}
          </li>
        ))}
      </ul>
    </main>
  );
}

// export async function getStaticProps() {
//   const { data } = await getClient().query({ query });

//   return {
//     props: {
//       airlines: data.airlines,
//     },
//   };
// }
