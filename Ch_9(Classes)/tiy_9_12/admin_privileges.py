from user import User

class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin can perform following actions: ")
        for privilege in self.privileges:
            print("\t",privilege)
    

class Admin(User):

    def __init__(self, first_name, last_name, age, gender, occupation, address):
        super().__init__(first_name, last_name, age, gender, occupation, address)
        self.privileges = Privileges(pri) 
        

pri = ['can add post', 'can delete post', 'can ban user']