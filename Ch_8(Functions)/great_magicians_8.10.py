magicians =['william','modi','trump','walker','op']

great_magicians =[]
def make_great(magicians):
    while magicians:
        magician = magicians.pop()
        great_magicians.append('the Great '+magician)


    show_magicians(great_magicians)



def show_magicians(magicians):
    for magician in magicians:
        print("Hello",magician.title())
    

make_great(magicians)
# show_magicians(magicians)