from flask import Blueprint, jsonify
import os
import boto3
from botocore.exceptions import ClientError

routes = Blueprint('api', __name__)

@routes.route("/secret")
def get_secret():
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region     = os.getenv('AWS_REGION')
    table_name = 'devops-challenge' 
    code_name = 'theDoctor'

    try:
        dynamodb = boto3.client(
            'dynamodb',
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )

        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'codeName': {'S': code_name}
            }
        )

        if 'Item' in response:
            return jsonify({
                'secret_code': response['Item']
            }), 200
        else:
            return jsonify({'error': 'Item not found'}), 404

    except ClientError as e:
        return jsonify({'error': e.response['Error']['Message']}), 500

@routes.route("/health")
def health_check():
    return jsonify({ 'status': 'healthy', 'container': 'https://hub.docker.com/r/yinonoz/devops-challenge', 'project': 'https://github.com/yinonozery/devops-challenge' })
