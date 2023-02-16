import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table=dynamodb.Table('houda')
    
    try:
        response=table.get_item(
        Key={
            'id':0
        }
        
        )
        my_count=response['Item']['counter']
        # TODO: write code...
    except:
        my_count=1
    
    new_counter=my_count+1
    
    #updating the table
    
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
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'total_visitor': str(new_counter)})
    }