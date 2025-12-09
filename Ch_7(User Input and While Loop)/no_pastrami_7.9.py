sandwich_orders =['club sandwich','pastrami','grilled cheese sandwich','pastrami','chicken sandwich','veg sandwich','pastrami','submarine sandwich']


print("Deli has run out of pastrami.")


finished_sandwiches =[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
        sandwiches = sandwich_orders.pop()
        print("I made : "+ sandwiches.title())
        finished_sandwiches.append(sandwiches)

print("\nFinished sandwiches are: ")
for sandwich in finished_sandwiches:
    print('\t'+sandwich.title())