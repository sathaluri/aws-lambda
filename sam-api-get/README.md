# Building and running sam-api-post-layers locally

## Description

* SAM (Serverless Application Model) project that creates a simple API that can be used to get records from a Postgres table. 
* The project includes a Lambda function that is triggered by API Gateway requests. 
* The Lambda function simply takes the queryStringParameters from the API Gateway and return the data from Postgres loans.Customer table.

## Prerequisites

* To build or run the project, you will need to have the SAM CLI installed. 

* Install and configure Docker if not already done.

* Postgres database running inside docker.

* The Postgres Database should have the table `loans.Customer`(You can find the schema in the scripts folder).

* Change the postgres `conn` variables in `api.get.py`

  ![template](/images/sam-api-get/image-1.png)
  
* Make sure you have the Docker network `tinitiate` set up. If you haven't created it yet, you can create it using the following command.

  ```bash
  docker network create tinitiate
  ```

## Steps to run the application locally

* Clone the repository by running the following command.

  ```bash
  git clone https://github.com/sathaluri/aws-lambda.git
  ```

* Change the directory to the cloned repository.

  ```bash
  cd sam-api-get
  ```

* Build the application using the following command.

  ```bash
  sam build
  ```

 * We can invoke the lambda function locally by using the following command.

   ```bash
   sam local start-api --docker-network tinitiate
   ```

* The API will be available at `http://localhost:3000/records`, and we can make a get request to insert data into the **tinitiate** database.
