import unittest
import multe

class TestMulte(unittest.TestCase):
	def test_multe_2_values(self):
self.assertEqual(multe.multe_2_values(3, 5), 15)