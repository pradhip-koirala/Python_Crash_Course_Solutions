players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) #start to 2 index.

print(players[1:4]) #form 1 to 3: 4 excluded

print(players[:4]) #0 to 3 index : 4 is excluded

print(players[2:])#strat from index 2 to last

print(players[-3:]) #last 3 elements


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
