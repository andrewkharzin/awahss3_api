import React, { useState } from "react";
// import "flowbite/dist/flowbite.css"; // Import Flowbite styles

interface DatePickerProps {
  onChange: (date: string) => void;
}

const DatePicker: React.FC<DatePickerProps> = ({ onChange }) => {
  const [selectedDate, setSelectedDate] = useState<string | undefined>(undefined);

  const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedDate(event.target.value);
    onChange(event.target.value);
  };

  return (
    <div className="input-group w-full">
      <input
        type="date"
        value={selectedDate || ''}
        onChange={handleDateChange}
        className="input datepicker-input" // Apply Flowbite classes
      />
    </div>
  );
};

export default DatePicker;
