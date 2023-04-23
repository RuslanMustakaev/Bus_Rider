"""The functionality for checking the correctness of buses data transmitted in JSON format passed to standard input"""

import json
import re
import itertools


class BusesData:
    """The creation of the Buses object and the related functionality."""
    # Required content and data type dictionary
    validation = {
        'bus_id': {'type': int, 're_pattern': r"\d+"},
        'stop_id': {'type': int, 're_pattern': r"\d+"},
        'stop_name': {'type': str, 're_pattern': r"([A-Z]\w+\s)+(Road|Avenue|Boulevard|Street)$"},
        'next_stop': {'type': int, 're_pattern': r"\d+"},
        'stop_type': {'type': str, 're_pattern': r"[SOF ]?"},
        'a_time': {'type': str, 're_pattern': r"((1\d)|(2[0-3])|(0\d)):([0-5]\d)"}
    }

    def __init__(self, data):
        self.buses_data = data
        self.errors_dict = dict.fromkeys(self.validation, 0)

    def check_bus_data(self) -> None:
        """Check required fields are filled and type of data"""
        for bus_data in self.buses_data:
            for key, value in bus_data.items():
                if not isinstance(value, self.validation[key]['type']) or \
                        re.fullmatch(self.validation[key]['re_pattern'], str(value)) is None:
                    self.errors_dict[key] += 1
        return None

    def show_data_validation(self):
        """Print quantity of data type errors and wrong fill of the fields"""
        print(f"Type and required field validation: {sum(self.errors_dict.values())} errors")
        for key, value in self.errors_dict.items():
            if value:
                print(f"{key}: {value}")

    def show_format_errors(self) -> None:
        """Check of the data format complies with the documentation requirements and print count of errors for fields

        Requirements for fields:\n
        'stop_name' - [proper name][suffix]
                      Suffix: Road|Avenue|Boulevard|Street
                      Proper name starts with the capital latter

        'stop_type' - S (for starting stop)
                      O (for stop on demand)
                      F (for final stop)

        'a_time'    - HH:MM (24-hour date format)"""
        fields_for_check_set = {'stop_name', 'stop_type', 'a_time'}
        print(f"Format validation: {sum(self.errors_dict.values())} errors")
        for error_field, errors_value in self.errors_dict.items():
            if error_field in fields_for_check_set:
                print(f"{error_field}: {errors_value}")
        return None

    @property
    def stop_names_for_buses(self) -> dict:
        """Generate dictionary with key - 'bus_id' and value - set of stops for this bus"""
        stop_names_for_buses_dict = dict()
        for bus_data in self.buses_data:
            stop_names_for_buses_dict.setdefault(bus_data["bus_id"], set()).add(bus_data["stop_name"])
        return stop_names_for_buses_dict

    def show_bus_stops_number(self) -> None:
        """Print quantity of stops for each bus in data"""
        print("Line names and number of stops:")
        for bus_id, stops_set in self.stop_names_for_buses.items():
            print(f"bus_id: {bus_id}, stops: {len(stops_set)}")
        return None

    @property
    def start_stops(self) -> set:
        """Collect set of start stops for all buses"""
        return {bus_data["stop_name"] for bus_data in self.buses_data if bus_data["stop_type"] == "S"}

    @property
    def finish_stops(self) -> set:
        """Collect set of finish stops for all buses"""
        return {bus_data["stop_name"] for bus_data in self.buses_data if bus_data["stop_type"] == "F"}

    @property
    def on_demand_stops(self) -> set:
        """Collect set of On-demand stops for all buses"""
        return {bus_data["stop_name"] for bus_data in self.buses_data if bus_data["stop_type"] == "O"}

    @property
    def transfer_stops(self) -> set:
        """Collect set of transfer stops between buses"""
        transfer_stops = set()
        transfer_iter = itertools.combinations(self.stop_names_for_buses.values(), 2)
        for stops_set in transfer_iter:
            if len(stops_set[0].intersection(stops_set[1])):
                transfer_stops.update(stops_set[0].intersection(stops_set[1]))
        return transfer_stops

    def show_stops(self) -> None:
        """Print lists of start, transfer, and finish stops"""
        print(f"Start stops: {len(self.start_stops)} {sorted(self.start_stops)}")
        print(f"Transfer stops: {len(self.transfer_stops)} {sorted(self.transfer_stops)}")
        print(f"Finish stops: {len(self.finish_stops)} {sorted(self.finish_stops)}")
        return None

    def start_finish_stops_checker(self):
        """Check that each bus line has exactly one starting point (S) and one final stop (F)"""
        stop_types_for_bus_dict = dict()
        for bus_data in self.buses_data:
            stop_types_for_bus_dict.setdefault(bus_data["bus_id"], set()).add(bus_data["stop_type"])

        for bus_id, stops_type_set in stop_types_for_bus_dict.items():
            if "S" not in stops_type_set or "F" not in stops_type_set:
                print(f"There is no start or end stop for the line: {bus_id}.")
                return None
            else:
                continue
        self.show_stops()

    @property
    def buses_arrival_time_dict(self) -> dict:
        """Generate dictionary with key - 'bus_id' and value - list of stop and arrival time"""
        stop_types_for_bus_dict = dict()
        for bus_data in self.buses_data:
            stop_types_for_bus_dict.setdefault(bus_data["bus_id"], list()).append([bus_data["stop_name"],
                                                                                   bus_data["a_time"]])
        return stop_types_for_bus_dict

    def arrival_time_validation(self):
        """Check that the arrival time for the upcoming stops for a given bus line is increasing.
        If bus have wrong arrival time, prints message with bus_id and stop name"""
        current_time = None
        wrong_arrival_stop = []
        print("Arrival time test:")
        for bus_id, stops_time_list in self.buses_arrival_time_dict.items():
            for stop in stops_time_list:
                if current_time is None:
                    current_time = stop[1]
                else:
                    if current_time > stop[1]:
                        print(f'bus_id line {bus_id}: wrong time on station {stop[0]}')
                        wrong_arrival_stop.append(stops_time_list[0])
                        current_time = None
                        break
                    else:
                        current_time = stop[1]
            current_time = None
        if not wrong_arrival_stop:
            print("OK")
            return None
        return None

    def wrong_stops_checker(self):
        """Check all the departure points, final stops, and transfer stations are not 'On-demand'
           Prints the unique names of the stops if that stops containing this type of issue."""
        wrong_stops = self.on_demand_stops.intersection(self.start_stops |
                                                        self.finish_stops |
                                                        self.transfer_stops)
        print("On demand stops test:")
        if wrong_stops:
            print(f"Wrong stop type: {sorted(wrong_stops)}")
        else:
            print("OK")


if __name__ == '__main__':
    routes = json.loads(input())
    buses = BusesData(routes)
    buses.check_bus_data()
    buses.show_format_errors()
    buses.show_bus_stops_number()
    buses.start_finish_stops_checker()
    buses.arrival_time_validation()
    buses.wrong_stops_checker()
