import unittest
import sub

class TestSubtract(unittest.TestCase):
	def test_subtract_2_values(self):
		self.assertEqual(sub.subtract_2_values(5, 3), 2)
