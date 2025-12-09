prompt = "\nEnter pizza toppings you onwould like: "
prompt += "\nEnter 'quit' if finished: "

#conditional test
toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print('\t',toppings.title(),'topping added.')


#use an active variable.
active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    else:
        print('\t',toppings.title(),'topping added.')

    
#using a break statement to stop looping.
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print('\t',toppings.title(),'topping added.')