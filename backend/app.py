from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from opensearchpy import OpenSearch
import os
import boto3


app = Flask(__name__)
app.secret_key = 'random_secret_key'
oauth = OAuth(app)

# Google OAuth configuration
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_params=None,
    client_kwargs={'scope': 'openid email profile https://www.googleapis.com/auth/gmail.readonly'},
)

# AMAZON S3 Buckets Client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# AWS Open Search client
opensearch_client = OpenSearch(
    hosts=[{'host': os.getenv("OPENSEARCH_HOST"), 'port': 443}],
    http_auth=(os.getenv("AWS_ACCESS_KEY_ID"), os.getenv("AWS_SECRET_ACCESS_KEY")),
    use_ssl=True,
    verify_certs=True
)

# Amazon SQS client
sqs_client = boto3.client(
    'sqs',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# S3 upload finction
def upload_file_to_s3(file_name):
    s3_client.upload_file(file_name, os.getenv("S3_BUCKET_NAME"), file_name)

# SQS message router function
def send_message_to_sqs(queue_url, message):
    response = sqs_client.send_message(QueueUrl=queue_url, MessageBody=message)
    return response

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    session['token'] = token
    return redirect('/')




