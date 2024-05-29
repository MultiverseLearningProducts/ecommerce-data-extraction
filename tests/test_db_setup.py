import unittest
from src.db_setup import create_db_and_tables

class TestDBSetup(unittest.TestCase):
    def test_create_db_and_tables(self):
        self.assertTrue(create_db_and_tables())

if __name__ == '__main__':
    unittest.main()
