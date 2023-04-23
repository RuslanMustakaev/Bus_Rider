from itertools import combinations

for r in range(1, 4):
    for bouquets in combinations(flower_names, r):
        print(bouquets)
