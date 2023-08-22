import React from "react";
import { useEffect } from "react";
import { Link } from "react-router-dom";
import "../../assets/css/megamenu.css";
import NavClock from "../ui/widgets/NavBarClock";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faPlaneArrival,
  faPlaneDeparture,
  faPlaneCircleExclamation,
} from "@fortawesome/free-solid-svg-icons";

const MegaMenuComponent: React.FC = () => {
  useEffect(() => {
    const handleShortcut = (event: KeyboardEvent) => {
      if (event.key === "f" && (event.metaKey || event.ctrlKey)) {
        // Check for Cmd or Ctrl key + F
        event.preventDefault(); // Prevent the default browser behavior (searching the page)
        // You can trigger the click on the link using its DOM element
        const linkElement = document.querySelector(
          'a[href="/schedules/freighters/table"]'
        );
        if (linkElement instanceof HTMLAnchorElement) {
          // Check if it's an anchor element
          linkElement.click();
        }
      }
      if (event.key === "a" && (event.metaKey || event.ctrlKey)) {
        // Check for Cmd or Ctrl key + F
        event.preventDefault(); // Prevent the default browser behavior (searching the page)
        // You can trigger the click on the link using its DOM element
        const linkElement = document.querySelector(
          'a[href="/schedules/arrival/table"]'
        );
        if (linkElement instanceof HTMLAnchorElement) {
          // Check if it's an anchor element
          linkElement.click();
        }
      }
    };

    window.addEventListener("keydown", handleShortcut);

    return () => {
      window.removeEventListener("keydown", handleShortcut);
    };
  }, []);
  return (
    <div className="sticky top-0 z-30 flex h-20 w-full justify-center text-base-content opacity-90 backdrop-blur transition-all duration-100">
      <nav className="navbar mx-auto flex w-full flex-wrap items-center justify-between bg-base-100 px-4 py-3">
        <div className="flex flex-1 md:gap-1 lg:gap-2">
          <Link
            to="/"
            aria-current="page"
            aria-label="Homepage"
            className="btn-ghost btn px-2"
          >
            <div className="inline-flex text-lg text-primary  md:text-2xl">
              <span className="uppercase text-orange-600">
                <span className="text-sm uppercase">AWAHS </span>
              </span>
              <span className="text-base-content">
                {" "}
                <span className="text-sm uppercase">Services</span>
              </span>
            </div>
          </Link>
        </div>
        <span className="badger bagdet-ghost text-sm font-light text-slate-500">
          <NavClock />
        </span>
        <div className="flex-none">
          <ul className="hoverable hover:bg-blue-800 hover:text-white">
            <input
              id="toggle-one"
              type="checkbox"
              value="selected"
              className="toggle-input"
            />
            <label
              htmlFor="toggle-one"
              className="btn-ghost btn gap-1 normal-case"
            >
              Services
            </label>
            <div
              role="toggle"
              className="mega-menu mb-16 bg-gray-800 p-6 shadow-xl sm:mb-0"
            >
              <div className="container flex w-full flex-wrap justify-between">
                <ul className="w-full border-b border-gray-600  py-6 sm:w-1/2 sm:border-r lg:w-1/4 lg:border-b-0 lg:pt-3">
                  <h3 className="text-bold mb-2 text-xl font-bold text-white">
                    <span className="text-xs font-normal uppercase text-accent">
                      iBase
                    </span>
                    <span className="ml-1 font-normal uppercase">Codes</span>
                  </h3>
                  <Link to="/ibase">
                    <li>
                      <span className="block p-3  text-gray-300 hover:bg-base-100 hover:text-accent">
                        IMP Codes
                      </span>
                    </li>
                  </Link>
                </ul>
                <ul className="w-full border-b border-gray-600 py-6 sm:w-1/2 sm:border-r lg:w-1/4 lg:border-b-0 lg:pt-3">
                  <h3 className="text-bold mb-2 text-sm font-bold text-white">
                    <span className="text-xs font-normal uppercase text-accent">
                      iSchedules
                    </span>
                    <span className="ml-1 font-normal uppercase">Flights</span>
                  </h3>
                  <Link to="/schedules/arrival/table">
                    <li>
                      <span className="block p-3 space-4-x text-gray-300 hover:bg-base-100 hover:text-accent">
                        <FontAwesomeIcon
                          icon={faPlaneArrival}
                          className="text-slate-400 mr-1"
                        />
                        Arrival (<kbd className="ml-2 kbd kbd-xs">cmd</kbd>+
                        <kbd className="mr-2 kbd kbd-xs">A</kbd>)
                      </span>
                    </li>
                  </Link>
                  <Link to="/schedules/arrival/table">
                    <li>
                      <span className="block p-3 space-4-x text-gray-300 hover:bg-base-100 hover:text-accent">
                        <FontAwesomeIcon
                          icon={faPlaneDeparture}
                          className="text-slate-400 mr-1"
                        />
                        Departure (<kbd className="ml-2 kbd kbd-xs">cmd</kbd>+
                        <kbd className="mr-2 kbd kbd-xs">D</kbd>)
                      </span>
                    </li>
                  </Link>
                  <Link to="/schedules/freighters/table">
                    <li>
                      <span className="block p-3  text-gray-300 hover:bg-base-100 hover:text-accent">
                        <FontAwesomeIcon
                          icon={faPlaneCircleExclamation}
                          className="text-slate-400 mr-1"
                        />
                        Freighters (<kbd className="ml-2 kbd kbd-xs">cmd</kbd>+
                        <kbd className="mr-2 kbd kbd-xs">F</kbd>)
                      </span>
                    </li>
                  </Link>
                </ul>
                <ul className="w-full border-b border-gray-600 px-4 py-6 sm:w-1/2 sm:border-r lg:w-1/4 lg:border-b-0 lg:pt-3">
                  <h3 className="text-bold mb-2 text-xl font-bold text-white">
                    <span className="text-xs font-normal  uppercase text-accent ">
                      Aviation
                    </span>
                    <span className="ml-1 font-normal uppercase">Codes</span>
                  </h3>
                  <Link to="/ibase/airports">
                    <li>
                      <span className="block p-3 text-gray-300 hover:bg-base-100 hover:text-accent">
                        Airports
                      </span>
                    </li>
                  </Link>
                  <Link to="/directory/airlines">
                    <li>
                      <span className="block p-3 text-gray-300 hover:bg-base-100 hover:text-accent">
                        Airlines
                      </span>
                    </li>
                  </Link>
                </ul>
              </div>
            </div>
          </ul>
        </div>

        <div></div>
      </nav>
    </div>
  );
};

export default MegaMenuComponent;
