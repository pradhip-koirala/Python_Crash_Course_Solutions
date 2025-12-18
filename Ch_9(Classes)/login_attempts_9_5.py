class User():

    def __init__(self,first_name, last_name,
                 age, gender, occupation, address):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.address = address
        self.login_attempts = 0
        self.full_name = self.first+ " " +self.last


    def describe_user(self):
        
        print("\nFull Name:", self.full_name.title())
        print("You are "+str(self.age) + " years old.")
        print("Sex:",self.gender)
        print("Occupation:",self.occupation.title())
        print("Location:",self.address.title())

    def greet_user(self):
        print(f"Hello",self.full_name.title(), "from "+self.address.title(),"\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts: ",self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Reseting login attempts to:",self.login_attempts)



user = User('zaw','htwe',21, 'male', 'student','myanmar')
# user.describe_user()
user.greet_user()
user.describe_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()

# second_user = User('optimus','prime', 10000, 'unknown', 'leader','cybertron')
# second_user.greet_user()
# second_user.describe_user()


# third_user =User('sofia','lee',34, 'female','manager','singapore')
# third_user.greet_user()
# third_user.describe_user()