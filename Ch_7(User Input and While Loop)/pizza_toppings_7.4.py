prompt = "\nEnter pizza toppings you onwould like: "
prompt += "\nEnter 'quit' if finished: "

toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print('\t',toppings.title(),'topping added.')
