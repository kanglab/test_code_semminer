import unittest
import divide

class TestDivide(unittest.TestCase):
	def test_divide_2_values(self):
		self.assertEqual(divide.divide_2_values( 9, 3), 3)
