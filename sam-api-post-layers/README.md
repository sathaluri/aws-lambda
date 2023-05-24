# Building and running sam-api-post-layers locally

## Description

* SAM (Serverless Application Model) project that creates a simple API that can be used to insert records into a Postgres table. 
* The project includes a Lambda function that is triggered by API Gateway requests. 
* The Lambda function simply takes the message body from the request and inserts it into the Postgres table.

## Prerequisites

* To build or run the project, you will need to have the SAM CLI installed. 

* Install and configure Docker if not already done.

* Postgres database running inside docker.

* The Postgres Database should have the table `shoppingcart.products`(You can find the schema in the scripts folder).

* Change the environment variables in `template.yml`

  ![template](/images/sam-api-post/image-1.png)

* Create a new directory for your layer.

  ```bash
  mkdir dependencies
  cd dependencies
  ```

* Create a `python` directory inside the layer directory.

  ```bash
  mkdir python
  cd python
  ```

* Install the dependencies using pip.

  ```bash
  pip install -r requirements.txt -t .
  ```

* Go back to the root directory of your SAM application.

  ```bash
  cd ../..
  ```

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
  cd aws-lambda/sam-api-post-layers
  ```

* Build the application using the following command.

* ```bash
  sam build
  ```

 * We can invoke the lambda function locally by using the following command.

   ```bash
   sam local start-api --docker-network tinitiate
   ```

* The API will be available at `http://localhost:3000/products`, and you can make a POST request to insert data into the **tinitiate** database.
* For testing this API we have to use `Postman` or any other `API Testing tool`.
* Please look at the image to how to do it with `Postman`.
   ![template](/images/sam-api-post/postman-1.png)
* Below is the sample json which has to be passed in Body as `raw`.
    ```json
      {
          "id":101,
          "category":"test", 
          "name":"test2", 
          "price":99.00
      }
    ```
* This should be the output.
    ![template](/images/sam-api-post/postman-2.png)
