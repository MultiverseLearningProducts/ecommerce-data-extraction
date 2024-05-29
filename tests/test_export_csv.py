import unittest
from src.export_csv import export_to_csv
from src.data_extraction import extract_and_join_data

class TestExportCSV(unittest.TestCase):
    def test_export_to_csv(self):
        data = extract_and_join_data()
        export_to_csv(data)
        with open('data/joined_data.csv', 'r') as file:
            content = file.read()
        self.assertTrue(len(content) > 0)

if __name__ == '__main__':
    unittest.main()
