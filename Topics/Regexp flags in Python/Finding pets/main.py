import re 

pets = input()
template = '(dog|cat|parrot|hamster)'
match = re.findall(template, pets, flags=re.I)
print(match)
