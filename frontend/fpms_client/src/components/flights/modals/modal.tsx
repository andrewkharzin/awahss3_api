//Modal.tsx
import React, { useRef } from "react";
import cn from "classnames";
import { useOnClickOutside } from "usehooks-ts";
import { FlightType } from "../../../types/flight/types";

interface FlightDetailModalProps {
  children: React.ReactNode;
  open: boolean;
  disableClickOutside?: boolean;
  flight: FlightType; // Replace 'Flight' with your actual flight interface
  onClose: () => void;
}

const FlightDetailModal = ({
  children,
  open,
  disableClickOutside,
  onClose,
}: FlightDetailModalProps) => {
  const ref = useRef(null);
  useOnClickOutside(ref, () => {
    if (!disableClickOutside) {
      onClose();
    }
  });

  const modalClass = cn({
    "modal modal-bottom sm:modal-middle": true,
    "modal-open": open,
  });
  return (
    <div className={modalClass}>
      <div className="w-1/2 bg-base-100 shadow-xl rounded-tl-lg rounded-br-3xl" ref={ref}>
        {children}
      </div>
    </div>
  );
};

export default FlightDetailModal;
