# Creating Lambda Function with S3 Event as trigger

## Using AWS Console

### Create a Lambda function.
* Go to the AWS Lambda console and click on the `Create function` button.
* In the `Function name` field, enter a name for your function.
* In the `Runtime` field, select `Python 3.9`.
* In the `Role` field, select a role that has permission to access S3.
* Click on the `Create function` button.

### Create an S3 bucket.
* Go to the Search in the console and search s3
* Click on the `Create bucket` button.
* In the `Bucket name` field, enter a name for your bucket.
* Select a region for your bucket.
* Click on the `Create` button.

### Configure the Lambda function to be triggered by S3 events.
* In the AWS Lambda console, click on the name of your function.
* In the `Triggers` section, click on the `Add trigger` button.
* In the `Event source` field, select "S3".
* In the `Bucket` field, select the S3 bucket that you created in the previous step.
* In the `Event type` field, select "ObjectCreated:Put".
* Click on the `Add trigger` button.

### Test the Lambda function.
* In the AWS Lambda console, click on the name of your function.
* In the `Test` section, click on the `Invoke` button.
* In the `Input` field, enter the following (Replace the key with your object key):
 ```shell
  {
    "key": "my-object.txt"
  }
 ```
