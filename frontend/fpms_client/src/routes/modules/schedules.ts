import ArrivalFlights from '../../pages/schedules/ArrivalPage';
import FreightersFlights from '../../pages/schedules/FreightersPage';
import CreateFreight from '../../pages/schedules/CreateFreight';
// import FlightGantt from '../../components/flights/FlightGantt';

const scheduleRoutes = [
  {
    path: '/schedules/arrival/table',
    component: ArrivalFlights,
  },
  {
    path: '/schedules/freighters/table',
    component: FreightersFlights,
  },
 
  {
    path: '/schedules/freighters/add',
    component: CreateFreight,
  },
];

export default scheduleRoutes;
