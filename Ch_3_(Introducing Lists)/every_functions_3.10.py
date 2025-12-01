countries =['myanmar','india','thailand','singapore','indonesia','brunai','nepal','butan','turkey']

#length function
print("Total countries:",len(countries))

#title function.
print("First country:",countries[0].title())

#adding element at last position
new_country = countries.append("denmark")
print(countries)

#adding using insert() at second position
inserting_new_country = countries.insert(1,"america")

#removing using del
del countries[3]
print(countries)

#removing pop method, second last element removed.
print("Removing second last country:",countries.pop(len(countries)-2))

#removing using 'remove()' 
countries.remove('india')
print(countries)

#temp sort 
print("Temporarily sorted: \n",sorted(countries))

#permanent sort 
countries.sort()
print("Permanent sort:",countries)

#reverse permanent sort
countries.sort(reverse=True)
print("Permanent sort:",countries)
