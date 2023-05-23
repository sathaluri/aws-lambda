
* SAM (Serverless Application Model) project that creates a simple API that can be used to insert records into a Postgres table. 
* The project includes a Lambda function that is triggered by API Gateway requests. 
* The Lambda function simply takes the message body from the request and inserts it into the Postgres table.
* We can build the project by using the following command.
* 
  ```shell
  sam build
  ```
* We can invoke the lambda function locally by using the following command.

  ```shell
  sam local invoke <options> <functionLogicalId>
  ```  
 * We can invoke the lambda function locally by using the following command.
 
    ```shell
    sam local start-api <options>
    ```
## Prerequisites
  * To build or deploy the project, you will need to have the SAM CLI installed. 
  * The Postgres Database should have the table `shoppingcart.products`(You can find the schema in the scripts folder).
  * Change the environment variables in template.yml
     
     ![template](/images/sam-api-post/image-1.png)
