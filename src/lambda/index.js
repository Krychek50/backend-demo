exports.handler = async (event, context, callback) => {
  const result = { "Items": [ { "id": 0, "name": "first" }, 
                              { "id": 1, "name": "second" }, 
                              { "id": 2, "name": "third" },
                              { "id": 3, "name": "fourth" }, 
                              { "id": 4, "name": "fifth" } 
                            ]};
  
	// JSON body response
  const response = {
    statusCode: 200,
    headers: {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE"
    },
    body: JSON.stringify(result)
  };

  return result;
};