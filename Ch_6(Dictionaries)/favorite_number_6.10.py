fav_numbers = {
    'jorden' : [3,42,9],
    'niggas' : [38,29,23],
    'bull' : [7,39],
    'messi' : [10,19,89],
    'andres' : [48,59],
}


for k, v in fav_numbers.items():
    if k:
        print("\n"+k.title(),'favourite numbers are :')
    for vs in v:
        print("\t",vs)