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




# class Privileges():

#     def __init__(self, privileges):
#         self.privileges = privileges

#     def show_privileges(self):
#         print("Admin can perform following actions: ")
#         for privilege in self.privileges:
#             print("\t",privilege)
    

# class Admin(User):

#     def __init__(self, first_name, last_name, age, gender, occupation, address):
#         super().__init__(first_name, last_name, age, gender, occupation, address)
#         self.privileges = Privileges(pri) 
        

# pri = ['can add post', 'can delete post', 'can ban user']
# second_user = User('optimus','prime', 10000, 'unknown', 'leader','cybertron')

# admin = Admin('optimus','prime', 10000, 'unknown', 'leader','cybertron')

# admin.privileges.show_privileges()