even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Re-write the rest of the code here using map() and filter() where possible
my_sum = list(map(lambda even_num, odd_num: even_num + odd_num, even, odd))

remainders = list(map(lambda number: number % 3, my_sum))

nonzero_remainders = list(filter(None, remainders))

# remainders_ = [x % 3 for x in my_sum]

# nonzero_remainders_ = [r for r in remainders_ if r]

# print(remainders_)
# print(remainders)
# print(nonzero_remainders)
# print(nonzero_remainders_)
