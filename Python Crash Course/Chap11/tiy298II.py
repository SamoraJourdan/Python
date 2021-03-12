import unittest
from tiy298 import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.employee = Employee('Sam', 'Jourdan', 1000)

	def test_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(6000, self.employee.salary)

	def test_custom_raise(self):
		self.employee.give_raise(2000)
		self.assertEqual(3000, self.employee.salary)
	

if __name__ == '__main__':
	unittest.main()		