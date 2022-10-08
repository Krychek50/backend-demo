#! /usr/bin/python3
import subprocess
import shlex
import sys
import os
from zipfile import ZipFile

if __name__ == '__main__':
  # arn for role
  cmd = shlex.split(f'aws iam get-role --role-name {sys.argv[1]}')
  ret = subprocess.run(cmd, capture_output=True)
  
  arn = ret.stdout.decode('utf-8').strip('\n')

  # function zip
  folder_path = os.path.join('src', 'lambda')
  with ZipFile('function.zip', 'w') as archive:  
    for filename in os.listdir(folder_path):
      archive.write(os.path.join(folder_path, filename), filename)

  # aws create-function
  cmd = shlex.split(f'aws lambda create-function --function-name {sys.argv[2]} \
                      --role {arn} --zip-file fileb://function.zip \
                      --runtime nodejs16.x --handler index.handler')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Created lambda function')

  # remove zip
  os.remove('function.zip')