prompt ="\nEnter your age to see the ticket price."
prompt +="\nEnter 'quit' if finished : "

flag = True

while flag:
    age = input(prompt)
    if age != 'quit':
        age =int(age)
        if age < 3:
            print("\nYou are free to enter.")
        elif age <= 12:
            print("\nYour ticket charge is $10.")
        else:
            print("\nYour ticket is $15.")