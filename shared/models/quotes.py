from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Crew:
    cleaners: int
    suggested_hours_per_cleaner: int
    total_crew_hours: int
    
    @staticmethod
    def from_dict(obj: Any) -> 'Crew':
        _cleaners = int(obj.get("cleaners"))
        _suggested_hours_per_cleaner = int(obj.get("suggested_hours_per_cleaner"))
        _total_crew_hours = int(obj.get("total_crew_hours"))        
        return Crew(_cleaners, _suggested_hours_per_cleaner, _total_crew_hours)

@dataclass
class Detail:
    item_number: int
    description: str
    crew_hours: int
    hourly_rate: float
    amount: float

    @staticmethod
    def from_dict(obj: Any) -> 'Detail':
        _item_number = int(obj.get("item_number"))
        _description = str(obj.get("description"))
        _crew_hours = int(obj.get("crew_hours"))
        _hourly_rate = float(obj.get("hourly_rate"))
        _amount = float(obj.get("amount"))
        return Detail(_item_number, _description, _crew_hours, _hourly_rate, _amount)

@dataclass
class Footer:
    subtotal: float
    tax_percent: int
    tax_amount: float
    total: float

    @staticmethod
    def from_dict(obj: Any) -> 'Footer':
        _subtotal = float(obj.get("subtotal"))
        _tax_percent = int(obj.get("tax_percent"))
        _tax_amount = float(obj.get("tax_amount"))
        _total = float(obj.get("total"))
        return Footer(_subtotal, _tax_percent, _tax_amount, _total)

@dataclass
class Header:
    title: str
    property: str
    client: str
    service: str
    crew: Crew

    @staticmethod
    def from_dict(obj: Any) -> 'Header':
        _title = str(obj.get("title"))
        _property = str(obj.get("property"))
        _client = str(obj.get("client"))
        _service = str(obj.get("service"))
        _crew = Crew.from_dict(obj.get("crew"))
        return Header(_title, _property, _client, _service, _crew)

@dataclass
class Input:
    header: Header
    tasks: List[str]
    notes: List[str] = None  # Optional field for additional notes  

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        _header = Header.from_dict(obj.get("header"))
        _tasks = [str(y) for y in obj.get("tasks")]
        _notes = [str(y) for y in obj.get("notes")] if obj.get("notes") is not None else None
        return Input(_header, _tasks, _notes)

@dataclass
class Output:
    header: Header
    details: List[Detail]
    footer: Footer
    notes: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Output':
        _header = Header.from_dict(obj.get("header"))
        _details = [Detail.from_dict(y) for y in obj.get("details")]
        _footer = Footer.from_dict(obj.get("footer"))
        _notes = [str(y) for y in obj.get("notes")]
        return Output(_header, _details, _footer, _notes)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# output = Output.from_dict(jsonstring)
