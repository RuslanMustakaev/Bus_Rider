# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
min_value = min(test_dict, key=test_dict.get)
print("min:", min_value)
max_value = max(test_dict, key=test_dict.get)
print("max:", max_value)
# Work with the 'test_dict'
