import unittest

from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.em = Employee('dao-keer', 20, 50000)
	
	def test_give_default_raise(self):
		self.em.give_raise()
		self.assertEqual(self.em.salary, 55000)

	def test_give_custom_raise(self):
		self.em.give_raise(10000)
                self.assertEqual(self.em.salary, 60000)
		
unittest.main()
