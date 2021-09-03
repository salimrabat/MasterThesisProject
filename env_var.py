import boto3 as boto3
from pymongo import MongoClient

s3 = boto3.client('s3')
bucket_name = 'harpocrates-files'
mongo_client = MongoClient('localhost')
db = mongo_client.files_index
test_folder_path = '/home/salim/Downloads/maildir'
