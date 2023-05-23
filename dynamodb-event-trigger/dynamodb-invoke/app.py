import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            # process the new row
            new_row = record['dynamodb']['NewImage']
            print(new_row)