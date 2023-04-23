import itertools

my_iter = itertools.combinations(teams, 2)

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
