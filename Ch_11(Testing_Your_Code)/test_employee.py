import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp = Employee('john', 'doe', 50000)
        
    def test_give_default_raise(self):
        
        self.emp.give_raise()
        self.assertEqual(self.emp.print_detail(), 'John Doe_55000')

    def test_give_custom_raise(self):
        
        self.emp.give_raise(8000)
        self.assertEqual(self.emp.print_detail(), 'John Doe_58000')
        
unittest.main()