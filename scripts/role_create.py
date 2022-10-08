#! /usr/bin/python3
import subprocess
import shlex
import sys

if __name__ == '__main__':
  # Create role
  cmd = shlex.split(f'aws iam create-role --role-name {sys.argv[1]} --assume-role-policy-document file://roles/trust-policy.json')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Created iam role')

  # Attach lambda execute policy
  cmd = shlex.split(f'aws iam attach-role-policy --role-name {sys.argv[1]} --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Attached lambda policy')

  # Attsach dynamodb policy
  cmd = shlex.split(f'aws iam attach-role-policy --role-name {sys.argv[1]} --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Attached dynamodb policy')