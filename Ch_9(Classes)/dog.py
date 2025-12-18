class Dog():
    
    def __init__(self, name, age):
        """initialize name and age arrtibutes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in a response to a command."""
        print(self.name.title()+ " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title()+ " is rolled over!")
    
my_dog = Dog('wilie', 6)

your_dog = Dog('lucy',3)

# my_dog.roll_over()

print("My dog's name is "+ my_dog.name.title()+ ".")
print("My dog is "+str(my_dog.age) + "years old.")
my_dog.sit()
my_dog.roll_over()

print("\nMy dog's name is "+ your_dog.name.title()+ ".")
print("My dog is "+str(your_dog.age) + "years old.")
your_dog.sit()
your_dog.roll_over()