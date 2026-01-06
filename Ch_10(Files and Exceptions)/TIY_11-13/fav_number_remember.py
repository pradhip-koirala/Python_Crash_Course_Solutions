import json

try:
    with open('favorite_number.json') as file:
        number = json.load(file)
        
except FileNotFoundError:
    username = input("Enter your name: ")

    with open('favorite_number.json', 'w') as file:
        json.dump(username, file)
        print("I'll remember your fav number when you come back.")
else:
    print("I know your favorite number! it's "+number)