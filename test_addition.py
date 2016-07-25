import unittest
import addition

class TestAddition(unittest.TestCase):
	def test_addition_2_values(self):
		self.assertEqual(addition.addition_2_values(3, 5), 8)