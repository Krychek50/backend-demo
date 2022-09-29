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
      "content-type": "json",
      "access-control-allow-origin": "*",
      "access-control-allow-headers": "*",
      "access-control-allow-methods": "OPTIONS, GET, POST, PUT, DELETE",
    },
    body: JSON.stringify(result)
  };

  return response;
};