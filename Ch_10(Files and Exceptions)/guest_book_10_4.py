with open('guest_book.txt', 'a') as file:
    flag = True
    while flag:
        
        name = input("Enter your name (q to quit): ")
        if name != 'q':
            file.write(f"Hello {name.title()}, Welcome!"+"\n")
            
        else:
            flag = False
        
