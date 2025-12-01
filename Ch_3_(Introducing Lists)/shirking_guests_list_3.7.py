guests = ['liam','noah','oliver','theodore','amelia','charlotte','emma']

print("Sorry, I can only got the table for two.")

popped_guest = guests.pop()
print("Sorry,",popped_guest.title(),"I only got the table for two.",)
popped_guest = guests.pop()
print("Sorry,",popped_guest.title(),"I only got the table for two.",)
popped_guest = guests.pop()
print("Sorry,",popped_guest.title(),"I only got the table for two.",)
popped_guest = guests.pop()
print("Sorry,",popped_guest.title(),"I only got the table for two.",)
popped_guest = guests.pop()
print("Sorry,",popped_guest.title(),"I only got the table for two.",)

#checking how many guest are still invited.
print("Remaining guests",guests)

print(guests[0].title(),"You are still invited.")
print(guests[1].title(),"You are still invited.")

#deleting all guesting , to empty list.
del guests[1]
del guests[0]
print(guests)