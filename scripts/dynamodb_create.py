#! /usr/bin/python3
import subprocess
import shlex
import sys

if __name__ == '__main__':
  # arn for role
  cmd = shlex.split(f'aws dynamodb create-table --cli-input-json file://schema/db-schema.json')

  ret = subprocess.run(cmd, capture_output=True)
  print(ret)