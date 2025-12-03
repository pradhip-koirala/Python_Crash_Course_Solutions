person_0 = {
    'first_name' : 'Michel',
    #key : value
    'last_name' : 'Jackson',
    'age' : 25,
    'city' : 'new york'
}

person_1 = {
    'first_name' : 'Lionel',
    'last_name' : 'Messi',
    'age' : 35,
    'city' : 'miami'
}

person_2 ={
    'first_name' : 'Cristiano',
    'last_name' : 'Ronaldo',
    'age' : 39,
    'city' : 'dubai'
}

people = [person_0,person_1,person_2]

i=1
for person in people:
    print((i),person)
    i += 1