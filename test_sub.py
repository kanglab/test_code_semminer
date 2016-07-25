import unittest
import sub

class TestSubtract(unittest.TestCase):
	def test_substract_2_values(self):
		self.assertEqual(sub.substract_2_values(5, 3), 2)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
