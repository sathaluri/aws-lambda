import csv

def process_csv(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Processing S3 object: {bucket}/{key}")
    
    # Read the CSV file
    with open(key, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    
    return {
        "statusCode": 200,
        "body": "Success"
    }
