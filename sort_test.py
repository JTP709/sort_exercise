import unittest
from sort import simpleSort

class SortTest(unittest.TestCase):
	def test_simple_sort(self):
		sortArray = ['1234','123','12345','1','12']

		result = simpleSort(sortArray)

		self.assertTrue(result[0] == '1')
		self.assertTrue(result[1] == '12')

	# def test_bubble_sort(self):

if __name__ == '__main__':
	unittest.main()
