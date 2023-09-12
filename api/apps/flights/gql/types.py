import strawberry
from strawberry import auto
from typing import List, Optional
from apps.flights.models.flight_model import CharterFlight
from apps.directory.airlines.models.airline import Airline, Aircraft
from apps.flights.models.file_model import File
from apps.flights.models.tripfile_model import TripFile, Msgs, Telex, Event, Attachment
from apps.flights.models.project import FlightProject
from api.apps.directory.airlines.gql.schema import AirlineType, AircraftType
from api.apps.users.gql.types import UserType


@strawberry.django.type(Msgs)
class MsgsType:
    tracking_date: str  # Assuming you want the date as a string
    tracking_time: str  # Assuming you want the time as a string
    author: UserType
    message: str


@strawberry.django.type(Telex)
class TelexType:
    message_type: str
    tracking_date: str
    tracking_time: str
    author: UserType
    message_content: str


@strawberry.django.type(Attachment)
class AttachmentType:
    # Reference to the TripFileType (if already defined)
    trip_file: 'TripFileType'
    file: 'FileType'  # Reference to the FileType (if already defined)


@strawberry.django.type(Event)
class EventType:
    event_date: str
    event_time: str
    event_type: str
    description: str
    author: UserType
    attachment: List[AttachmentType]


@strawberry.django.type(File)
class FileType:
    name: str
    file_url: str  # URL to access the file
    # Reference to the FlightProjectType (if already defined)
    # flight_project: 'FlightProjectType'

    @strawberry.field
    def get_full_path(self) -> str:
        return f'flights/{self.flight_project.flight.flight_number}{self.flight_project.flight.date.strftime("%Y-%m-%d")}/files/{self.name}'

    @strawberry.field
    def get_file_size(self) -> int:
        if self.file and hasattr(self.file, 'size'):
            return self.file.size
        return 0


@strawberry.django.type(Attachment)
class AttachmentType:
    file: FileType


# Decorate the TripFile model with strawberry
@strawberry.django.type(TripFile)
class TripFileType:
    msg: MsgsType
    telex: TelexType
    event: EventType
    attachment: AircraftType
    

@strawberry.django.type(CharterFlight)
class CharterFlightType:
    airline: AirlineType
    aircraft: AircraftType
    tripfile: TripFileType
    flight_number: str
    flight_date: Optional[str]
    flight_time: Optional[str]
    aircraft_type: Optional[str]
    registration_number: Optional[str]
    flight_route: Optional[str]
    iata: Optional[str]
    icao: Optional[str]
    action_code: Optional[str]
    slot_msg: Optional[str]
    state_status: str
    hand_status: str
    trip_status: str  # Note the quotes here

# Define the FlightProject model type

