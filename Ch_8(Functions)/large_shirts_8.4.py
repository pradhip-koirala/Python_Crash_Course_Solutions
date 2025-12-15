def make_shirt(message,size='large'):
    print("The shirt size is "+ size)
    print("The message is",message)

make_shirt("I love python.")#default size


#default message
def make_shirt(size,message='I love python'):
    print("\nThe shirt size is "+ size)
    print("The message is",message)

make_shirt("medium")

def make_shirt(size,message='I love python'):
    print("\nThe shirt size is "+ size)
    print("The message is",message)

make_shirt("large")
