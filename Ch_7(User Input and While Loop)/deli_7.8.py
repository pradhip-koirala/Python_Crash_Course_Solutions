sandwich_orders =['club sandwich','grilled cheese sandwich','chicken sandwich','veg sandwich','submarine sandwich']

finished_sandwiches =[]
while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print("I made : "+ sandwiches.title())
    finished_sandwiches.append(sandwiches)

print("\nFinished sandwiches are: ")
for sandwich in finished_sandwiches:
    print('\t'+sandwich.title())
