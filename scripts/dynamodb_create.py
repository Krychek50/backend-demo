#! /usr/bin/python3
import subprocess
import shlex
import json
import os

if __name__ == '__main__':
  # create table
  cmd = shlex.split(f'aws dynamodb create-table --cli-input-json file://schema/db-schema.json')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Created dynamodb table')

  # Load initial list of items
  with open(os.path.join('config', 'dbitems', 'populate.json'), 'r') as json_file:
    items = json.load(json_file)
  
  # Add Items
  for item in items:
    cmd = shlex.split(f'aws dynamodb put-item --table-name backend-demo-db --item')
    cmd.append(json.dumps(item))
    ret = subprocess.run(cmd, capture_output=True)
    if ret.returncode != 0:
      print(ret.stderr.decode('utf-8'))
    else:
      print(f'Added item {item}')