import unittest
from src.upload_to_s3 import upload_to_s3

class TestUploadToS3(unittest.TestCase):
    def test_upload_to_s3(self):
        response = upload_to_s3('data/joined_data.csv', 'your-bucket-name')
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
