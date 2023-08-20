import ArrivalFlights from '../../pages/schedules/ArrivalPage';
import FreightersFlights from '../../pages/schedules/FreightersPage';

const scheduleRoutes = [
  {
    path: '/schedules/arrival/table',
    component: ArrivalFlights,
  },
  {
    path: '/schedules/freighters/table',
    component: FreightersFlights,
  },
];

export default scheduleRoutes;
