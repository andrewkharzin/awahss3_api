import React, { useState, useEffect } from 'react';
import './clock.css'; // Import your

const DigitalClock: React.FC = () => {
    const [currentTime, setCurrentTime] = useState<string>(getFormattedTime());
    const [isBlinking, setIsBlinking] = useState<boolean>(false);
  
    useEffect(() => {
      const interval = setInterval(() => {
        setCurrentTime(getFormattedTime());
      }, 1000);
  
      const blinkInterval = setInterval(() => {
        setIsBlinking((prevIsBlinking) => !prevIsBlinking);
      }, 500);
  
      return () => {
        clearInterval(interval);
        clearInterval(blinkInterval);
      };
    }, []);
  
    function getFormattedTime(): string {
      const now = new Date();
      const hours = String(now.getHours()).padStart(2, '0');
      const minutes = String(now.getMinutes()).padStart(2, '0');
      const seconds = String(now.getSeconds()).padStart(2, '0');
      return `${hours}:${minutes}:${seconds}`;
    }
  
    return (
        <div className="flex items-center space-x-2">
            <button className="btn btn-active font-mono text-bold text-accent text-sm">

            <span>{currentTime.slice(0, 2)}</span>
            <span className={`time ${isBlinking ? 'blink' : ''}`}>:</span>
            <span>{currentTime.slice(3, 5)}</span>
            </button>
            
        </div>
    
    );
  };
  
  export default DigitalClock;