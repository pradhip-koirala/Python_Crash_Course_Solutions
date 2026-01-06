import json



with open('username.json') as file:
    username= json.load(file)
    print("Welcome back, "+ username + "!")