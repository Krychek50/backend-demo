# backend-demo
Demo project for AWS services, uses API Gateway to create a CRUD API with a Lambda integration with DynamoDB.

## Project
* *config*
  - *dbitems* \
Intital Database items
  - *roles* \
IAM policy
  - *schema* \
Database schema
* *scripts* \
Python setup scripts for AWS CLI
* *src* 
  - lambda \
Lambda sourcecode
* *tests* 
Postman collection for testing API routes

## Setup 
`yarn iam:create` \
`yarn dynamodb:create` \
`yarn dynamodb:populate` \
`yarn lambda:create` \
`yarn apigateway:create` 

## Update
`yarn lambda:update`

## Testing
`yarn postman:test`
