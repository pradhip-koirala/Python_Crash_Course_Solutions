import json

with open('file_json.json') as file:
    numbers = json.load(file)

print(numbers)