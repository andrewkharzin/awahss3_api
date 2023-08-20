// actions.ts
export const UPDATE_FILTERS = 'UPDATE_FILTERS';

export const updateFilters = (filters: {
  iatacodeFilter: string | null;
  flightTypeFilter: string | null;
  dateFilter: string | null;
}) => {
  return {
    type: UPDATE_FILTERS,
    payload: filters,
  };
};
