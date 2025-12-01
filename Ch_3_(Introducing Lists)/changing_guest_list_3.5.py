guests = ['liam','noah','oliver','theodore','amelia','charlotte','emma']


#removing 'oliver' from list.
removed_guest = guests.pop(2)
print("Unfortunately,",removed_guest.title(),"could not make it.")

#can also remove with 
# 'del guests[2]'
# guests.remove("oliver")

#adding new guest.
new_guest=guests.append("Sofia")

print("I would like to invite you to dinner",guests[0].title()+".")
print("I would like to invite you to dinner",guests[1].title()+".")
print("I would like to invite you to dinner",guests[2].title()+".")
print("I would like to invite you to dinner",guests[3].title()+".")
print("I would like to invite you to dinner",guests[4].title()+".")
print("I would like to invite you to dinner",guests[5].title()+".")
print("I would like to invite you to dinner",guests[6].title()+".")
