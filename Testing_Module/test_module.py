import unittest

from Testing_Module.my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_tuple_int(self):
        data = (4, 5, 6)
        result = sum(data)
        self.assertEqual(result, 15)

if __name__ == "__main_":
    unittest.main()