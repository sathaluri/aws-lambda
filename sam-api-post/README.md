* SAM (Serverless Application Model) project that creates a simple API that can be used to post messages to a DynamoDB table. 
* The project includes a Lambda function that is triggered by API Gateway requests. 
* The Lambda function simply takes the message body from the request and inserts it into the DynamoDB table.
* To build or deploy the project, you will need to have the SAM CLI installed. 
* We can build the project by using the following command.

  ```shell
  sam build
  ```
* We can invole the lambda function locally by using the following command.

  ```shell
  sam local invoke <options> <functionLogicalId>
  ```  
 * We can invole the lambda function locally by using the following command.
 
    ```shell
    sam local start-api <options>
    ```
