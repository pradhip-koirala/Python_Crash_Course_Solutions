class Employee:

    def __init__(self,first_name, last_name, anu_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.anu_salary = anu_salary
        
    def give_raise(self, amount = 5000):
        self.anu_salary += amount

    def print_detail(self):
        full_name = self.first_name+ " " + self.last_name
        return full_name.title()+ "_"+ str(self.anu_salary)
    
# emp = Employee('john', 'doe', 5000)
# emp.print_detail()