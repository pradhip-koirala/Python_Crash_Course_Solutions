locations = ['paris','bangkok','london','dubai','singapore','kula lumpur','new york','istanbul','atalya']

print("\nOriginal list\n",locations)

#using sorted() function to temporarily sort list.
print("\nTemporarily sorted locations:\n",sorted(locations))

locations.reverse()
print("\nReverse list:\n",locations)

locations.reverse()
print("\nReverse(second time) list:\n",locations)

#using sort to sort permanently.
locations.sort()
print("\nPermanently sorted list:\n",locations)

#permanent sort in reverse order.
locations.sort(reverse=True)
print("\nPermanently sorted list:\n",locations)
