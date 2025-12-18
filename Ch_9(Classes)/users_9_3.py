class User():

    def __init__(self,first_name, last_name,
                 age, gender, occupation, address):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.address = address
        self.full_name = self.first+ " " +self.last


    def describe_user(self):
        
        print("\nFull Name:", self.full_name.title())
        print("You are "+str(self.age) + " years old.")
        print("Sex:",self.gender)
        print("Occupation:",self.occupation.title())
        print("Location:",self.address.title())

    def greet_user(self):
        print(f"Hello",self.full_name.title(), "from "+self.address.title(),"\n")


user = User('zaw','htwe',21, 'male', 'student','myanmar')
# user.describe_user()
user.greet_user()
user.describe_user()

second_user = User('optimus','prime', 10000, 'unknown', 'leader','cybertron')
second_user.greet_user()
second_user.describe_user()


third_user =User('sofia','lee',34, 'female','manager','singapore')
third_user.greet_user()
third_user.describe_user()