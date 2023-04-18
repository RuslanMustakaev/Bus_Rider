"""The functionality for checking the correctness of buses data transmitted in JSON format passed to standard input"""

import json
import re
from collections import defaultdict
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


errors_dict = dict()  # Just for fix errors


def format_errors():
    fields_for_check_set = {'stop_name', 'stop_type', 'a_time'}
    print(f"Format validation: {sum(errors_dict.values())} errors")
    for error_field, errors_value in errors_dict.items():
        if error_field in fields_for_check_set:
            print(f"{error_field}: {errors_value}")


def count_bus_stops_number():
    bus_counter = {}
    print("Line names and number of stops:")
    for route in routes:
        for key, value in route.items():
            if key == 'bus_id':
                if bus_counter.get(value) is None:
                    bus_counter[value] = 1
                else:
                    bus_counter[value] += 1
    print(bus_counter)


def represent_stop(start_stop: set, transfer_stop: set, finish_stop: set) -> None:
    print(f"Start stops: {len(start_stop)} {sorted(list(start_stop))}")
    print(f"Transfer stops: {len(transfer_stop)}  {sorted(list(transfer_stop))}")
    print(f"Finish stops: {len(finish_stop)} {sorted(list(finish_stop))}")
    return None


def transfer_stops_find() -> set:
    stop_names_for_bus_dict = dict()
    transfer_stops = set()
    for bus_data in routes:
        stop_names_for_bus_dict.setdefault(bus_data["bus_id"], set()).add(bus_data["stop_name"])

    transfer_iter = itertools.combinations(stop_names_for_bus_dict.values(), 2)

    for stops_set in transfer_iter:
        if len(stops_set[0].intersection(stops_set[1])):
            transfer_stops.update(stops_set[0].intersection(stops_set[1]))
    return transfer_stops


def start_finish_stops_checker():
    check_set = {"S", "F"}
    start_stops_set = set()
    transfer_stops_set = set()
    finish_stop_set = set()
    stop_types_for_bus_dict = dict()
    for bus_data in routes:
        stop_types_for_bus_dict.setdefault(bus_data["bus_id"], set()).add(bus_data["stop_type"])
        if bus_data["stop_type"] == "S":
            start_stops_set.add(bus_data["stop_name"])
        elif bus_data["stop_type"] == "F":
            finish_stop_set.add(bus_data["stop_name"])
    for bus_id, types_of_stops in stop_types_for_bus_dict.items():
        # print(types_of_stops)
        set_that = types_of_stops.intersection(check_set)
        # print(set_that, "!!!")
        if "S" not in set_that or "F" not in set_that:
            print(f"There is no start or end stop for the line: {bus_id}.")
            # exit()
            return None
        else:
            continue
    transfer_stops_set.update(transfer_stops_find())
    represent_stop(start_stops_set, transfer_stops_set, finish_stop_set)


def check_bus_arrival_time(buses_data):
    current_bus_id = None
    current_time = None
    wrong_arrival_time = False
    wrong_arrival_stop = []
    print("Arrival time test:")
    for data_line in buses_data:
        if current_bus_id is None:
            current_bus_id = data_line["bus_id"]
            current_time = data_line["a_time"]
            continue
        else:
            if current_bus_id == data_line["bus_id"]:
                if not wrong_arrival_time:
                    if data_line["a_time"] > current_time:
                        current_time = data_line["a_time"]
                    else:
                        wrong_arrival_time = True
                        print(f'bus_id line {current_bus_id}: wrong time on station {data_line["stop_name"]}')
                        wrong_arrival_stop.append(data_line["stop_name"])
                        continue
                else:
                    continue
            else:
                current_bus_id = data_line["bus_id"]
                current_time = data_line["a_time"]
                wrong_arrival_time = False
                continue
    if len(wrong_arrival_stop) == 0:
        print("OK")


def wrong_stops_checker():
    wrong_stops = set()
    all_stops_name_dict = dict()
    for bus_data in routes:
        all_stops_name_dict.setdefault(bus_data["stop_type"], set()).add(bus_data["stop_name"])
    demand_stops = all_stops_name_dict['O']
    del all_stops_name_dict['O']
    for stop_name in all_stops_name_dict.values():
        if len(demand_stops.intersection(stop_name)):
            wrong_stops.update(demand_stops.intersection(stop_name))
    if len(wrong_stops):
        print("On demand stops test:")
        print("Wrong stop type: {wrong_stops_list}".format(wrong_stops_list=sorted(list(wrong_stops))))
    else:
        print("On demand stops test:")
        print("OK")


if __name__ == '__main__':
    routes = json.loads(input())
    buses = BusesData(routes)
    buses.show_data_validation()
    # check_bus_data(routes)
    # format_errors()
    # count_bus_stops_number()
    # start_finish_stops_checker()
    # check_bus_arrival_time(routes)
    # wrong_stops_checker()
