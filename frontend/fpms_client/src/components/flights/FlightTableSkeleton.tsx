import React from 'react';
import './skeleton.css';


const FlightTableSkeleton: React.FC = () => {
  return (
    <div className="w-full overflow-x-auto shadow animate-pulse ">
      
      <div className="w-full overflow-x-auto py-10 mx-2">
    
          <table className="w-full table-auto table-zebra">
            <thead>
              <tr>
              <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Planning Flight Time and Date">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                          </th>
                          <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Planning Flight Time and Date">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                          </th>
                          <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Planning Flight Time and Date">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                </th>
               
                <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Planning Flight Time and Date">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                </th>
                <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Arrival or Departure">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                </th>
                <th className="p-2 text-left text-sm uppercase">
                  <div className="tooltip" data-tip="Handling status">
                    <button className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5"></button>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>

                <tr
                  
                  
                >
                  <td className="px-2 py-2">
                    <div className="flex items-center space-x-3">
                      <div className="avatar">
                        <div className="w-8 rounded">
                          
                        </div>
                      </div>
                      <div>
                        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5">
                          
                        </div>
                        <div className="w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700">
                          
                        </div>
                      </div>
                    </div>
                  </td>
                  <td className="px-2 text-left">
                    <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5 text-left">
                      
                    </div>
                
                  </td>
                  <td className="p-2 text-left">
                    
                      
                        <div className="w-10 h-2 bg-gray-200 rounded-full dark:bg-gray-700"></div>

                  </td>
                  <td className="p-2 text-left font-normal text-slate-500">
                    <div className="w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700">
                     
                      
                    </div>
                  </td>
                  <td className="p-2 text-left">
                    <div className="w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700">
                      
                    </div>
                  </td>
                  <td className="p-2">
                    
                    
                    
                     
                    
                     
                        
                        <div className="w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700">
                          
                        </div>
                     
                    
                  </td>
                </tr>

            </tbody>
          </table>
      
      </div>
    </div>
  );
};

export default FlightTableSkeleton;
