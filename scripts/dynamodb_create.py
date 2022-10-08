#! /usr/bin/python3
import subprocess
import shlex
import sys

if __name__ == '__main__':
  # create table
  cmd = shlex.split(f'aws dynamodb create-table --cli-input-json file://schema/db-schema.json')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Created dynamodb function')