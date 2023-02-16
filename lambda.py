import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table=dynamodb.Table('houda')
    
    response=table.get_item(
        Key={
            'id':0
        }
        
        )
        
        
    table.update_item(
        Key={
         'id': 0,
            
        },
    UpdateExpression='SET #counter = :val1',
    ExpressionAttributeValues={
         ':val1': response['Item']['counter']+1
        
    },
    ExpressionAttributeNames={
    "#counter": "counter"
        
    }

    )
    return {
        'statusCode': 200,
        'body': json.dumps('counter incremented successfully')
    }