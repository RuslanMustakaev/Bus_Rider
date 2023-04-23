import itertools

# names = ['Jack', 'Michael', 'Ann', 'Jane']
names.sort()
for key, group in itertools.groupby(names, key=lambda x: x[0]):
    print(list(group))
