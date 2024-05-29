import unittest
from src.data_extraction import extract_and_join_data

class TestDataExtraction(unittest.TestCase):
    def test_extract_and_join_data(self):
        data = extract_and_join_data()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
