magicians =['william','modi','trump','walker','op']

great_magicians =[]
def make_great(magicians):
    while magicians:
        magician = magicians.pop()
        great_magicians.append('the Great '+magician)

    # print(great_magicians)

    return great_magicians




def show_magicians(magicians):
    for magician in magicians:
        print("Hello",magician.title())


print("Original Magicians")
show_magicians(magicians)

    
print("The great Magicians")
print(make_great(magicians[:]))