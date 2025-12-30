with open('guest.txt', 'a') as file:
    name = input("Enter your name: ")
    file.write(name+"\n")
