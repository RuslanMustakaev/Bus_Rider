import json
import re
from collections import defaultdict
import itertools

validation = {
    'bus_id': {'type': int, 're_pattern': r"\d+"},
    'stop_id': {'type': int, 're_pattern': r"\d+"},
    'stop_name': {'type': str, 're_pattern': r"([A-Z]\w+\s)+(Road|Avenue|Boulevard|Street)$"},
    'next_stop': {'type': int, 're_pattern': r"\d+"},
    'stop_type': {'type': str, 're_pattern': r"[SOF ]?"},
    'a_time': {'type': str, 're_pattern': r"((1\d)|(2[0-3])|(0\d)):([0-5]\d)"}
}

errors_dict = dict.fromkeys(validation, 0)


def check_bus_data(bus_info: dict):
    global errors_dict
    for route in bus_info:
        for key, value in route.items():
            if not isinstance(value, validation[key]['type']) or \
                    re.fullmatch(validation[key]['re_pattern'], str(value)) is None:
                # print(value)
                errors_dict[key] += 1


def type_validation_errors():
    print(f"Type and required field validation: {sum(errors_dict.values())} errors")
    for k, v in errors_dict.items():
        if v:
            print(f"{k}: {v}")


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


if __name__ == '__main__':
    routes = json.loads(input())
    # check_bus_data(routes)
    # format_errors()
    # count_bus_stops_number()
    start_finish_stops_checker()
