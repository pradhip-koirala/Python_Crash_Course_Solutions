import json


def get_stored_username():
    '''get stored username if available'''
    file_name = 'username.json'
    try:
        with open(file_name) as file:
            username = json.load(file)
            
    except FileNotFoundError:
        return None
    
    return username
    # else:
    #     return username


def get_new_username():
    '''prompt for a new username.'''
    username = input("what is your name? ")
    file_name = 'username.json'
    with open(file_name, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    print(username)
    check_username = input(f"Is this correct user name '{username.title()}' (yes/no): ")
    if check_username == 'no':
        username = get_new_username()
    elif check_username.lower() in ('yes', 'y'):
        print("Welcome back, " + username.title() +"!")
    
    
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() + "!")

        

greet_user()