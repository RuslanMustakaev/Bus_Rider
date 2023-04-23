def select_dates(potential_dates):
    target_age = 30
    names_list = [person["name"] for person in potential_dates
                  if person["age"] > target_age
                  and "art" in person["hobbies"]
                  and person["city"] == "Berlin"]
    return ", ".join(names_list)
