import re

string = input()
template = r"\+(\d)[-| ]?(\d{3})[ |-]?([\d -]*)"
match = re.match(template, string)
if not match:
    print("No match")
else:
    print("Full number:", string)
    print("Country code:", match.group(1))
    print("Area code:", match.group(2))
    print("Number:", match.group(3))
