import configparser
import boto3
from botocore.exceptions import NoCredentialsError

config = configparser.ConfigParser()
config.read('config.ini')

bucket_name = config.get('aws', 'bucket_name')

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print("Upload Successful")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == '__main__':
    upload_to_s3('data/joined_data.csv', bucket_name)
