import re

user_input = input()

match = re.findall('(\w+)', user_input, flags=re.A)
print(match)
