import json
numbers = [3,45,63,829,383,94,291,48]
with open('file_json.json', 'w') as file:
    json.dump(numbers,file)
