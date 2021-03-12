class Employee:
	def __init__(self, fn, ln, salary):
		self.fn = fn
		self.ln = ln
		self.salary = salary

	def give_raise(self, amount = 5000):
		self.salary += amount