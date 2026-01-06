import json

try:
    with open('favorite_number.json') as file:
        num = json.load(file)
        
except FileNotFoundError:
    pass
    
print("I know your favorite number! it's "+num)