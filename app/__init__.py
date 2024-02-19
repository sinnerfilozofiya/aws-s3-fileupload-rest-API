import os
import boto3
from flask import Flask
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '../credentials/.env'))
Bucket_name=os.getenv('AWS_S3_BUCKET_NAME')
# Setup AWS s3 Bucket connection
s3 = boto3.client('s3')


from app import routes