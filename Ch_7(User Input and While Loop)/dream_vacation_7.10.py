dream_places = {}

polling = True

while polling:
    name= input(("\nWhat is your name: "))
    place = input("Dream place like to visit: ")
    
    dream_places[name] = place

    repeat = input("Would you like to let another person respond? (yes(y)/ no(n)) ")
    if repeat in ('no','n'):
        polling = False


print("\n____Polling Results____")
for name, place in dream_places.items():
    print(name.title()+' would like to visit '+place.title())