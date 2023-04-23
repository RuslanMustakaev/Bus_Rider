import itertools

countries.sort(key=lambda x: x["population_mil"] > 100, reverse=True)
for population, country in itertools.groupby(countries, key=lambda x: x["population_mil"] > 100):
    if population:
        print(len(list(country)))
# print(len(list(filter(lambda x: x['population_mil'] > 100, countries))))
