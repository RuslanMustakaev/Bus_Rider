import re

template = r'are you ready??.?.?'
input_string = input()
match = re.match(template, input_string)
print(match.end() if match else "0")
