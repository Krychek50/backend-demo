const AWS = require("aws-sdk");
const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context, callback) => {  
  let result = {};
  let statusCode = 200;

  const TableName = "backend-demo-db";

  switch (event.routeKey) {
    case "POST /": {
        await dynamo.put({TableName, Item: JSON.parse(event.body)}).promise();
      }
      break;

    case "GET /": {
        const query = await dynamo.scan({ TableName }).promise();
        result = query.Items
      }
      break;

    case "GET /{id}": {
        const query = await dynamo.get({ TableName, Key: { Id: event.pathParameters.id }}).promise();
        result = query.Item
      }
      break;

    case "PUT /{id}": {
        await dynamo.put({TableName, Item: JSON.parse(event.body) }).promise();
      }
      break;

    case "DELETE /{id}": {
        await dynamo.delete({TableName, Key: { Id: event.pathParameters.id }}).promise();
      }
      break;

    case "OPTIONS /":
    case "OPTIONS /{id}":
    case "OPTIONS /{proxy+}":
      break;

    default:

      statusCode = 400;
      break;
  }

  // JSON body response
  const response = {
    statusCode,
    headers: {
      "content-type": "json",
      "access-control-allow-origin": "*",
      "access-control-allow-headers": "*",
      "access-control-allow-methods": "GET, POST, PUT, DELETE",
    },
    body: JSON.stringify(result)
  };

  return response;
};