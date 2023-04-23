import re


# put your regex in the variable template
template = "(Value|Name|Type)"
string = input()
match = re.match(template, string)
print(match.group() if match else None)
