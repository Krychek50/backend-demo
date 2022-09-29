#! /usr/bin/python3
import subprocess
import shlex
import sys
import json

if __name__ == '__main__':
  lambda_name = sys.argv[1]
  api_name = sys.argv[2]

  # Get FunctionArn
  cmd = shlex.split(f'aws lambda get-function --function-name {lambda_name}')
  ret = subprocess.run(cmd, capture_output=True)

  data = json.loads(ret.stdout)
  lambda_arn = data["Configuration"]["FunctionArn"]

  # aws apigatewayv2 create-api
  cmd = shlex.split(f'aws apigatewayv2 create-api --name {api_name} --protocol-type HTTP --target {lambda_arn}')
  ret = subprocess.run(cmd, capture_output=True)

  # Get api_id
  cmd = shlex.split(f'aws apigatewayv2 get-apis')
  ret = subprocess.run(cmd, capture_output=True)

  data = json.loads(ret.stdout)
  for item in data["Items"]:
    if item["Name"] == api_name:
      api_id = item["ApiId"]
      break

  # Get integration_id
  cmd = shlex.split(f'aws apigatewayv2 get-integrations --api-id {api_id}')
  ret = subprocess.run(cmd, capture_output=True)

  data = json.loads(ret.stdout)
  integration_id = data["Items"][0]["IntegrationId"]

  # Get account_id
  cmd = shlex.split(f'aws sts get-caller-identity')
  ret = subprocess.run(cmd, capture_output=True)

  data = json.loads(ret.stdout)
  account_id = data["Account"]

  # aws lambda add-permission
  source_arn = f"arn:aws:execute-api:eu-west-2:{account_id}:{api_id}/*/*/"
  cmd = shlex.split(f'aws lambda add-permission --function-name {lambda_arn} --action lambda:InvokeFunction --statement-id {api_name} --principal apigateway.amazonaws.com --source-arn {source_arn}')
  ret = subprocess.run(cmd, capture_output=True)

  # aws apigatewayv2 create-route
  routes = ['OPTIONS /', 'GET /', 'POST /', 'PUT /{id}', 'DELETE /{id}']
  for route in routes:
    cmd = shlex.split(f'aws apigatewayv2 create-route --api-id {api_id} --route-key route --target integrations/{integration_id}')
    cmd[6] = route
    ret = subprocess.run(cmd, capture_output=True)