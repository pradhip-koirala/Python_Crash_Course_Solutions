names =[]
#'john', 'optimus', 'prime', 'admin','pogba'

if names:
    for name in names:
        if name == 'admin':
            print("Hello",name.title(),"Would you like to see a status report.")
        else:
            print("Hello",name.title(),"Welcome!.")
else:
    print("We need to find some users!")
