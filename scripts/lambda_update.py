#! /usr/bin/python3
import subprocess
import shlex
import sys
import os
import json
from zipfile import ZipFile

if __name__ == '__main__':
  # function zip
  folder_path = os.path.join('src', 'lambda')
  with ZipFile('function.zip', 'w') as archive:  
    for filename in os.listdir(folder_path):
      archive.write(os.path.join(folder_path, filename), filename)

  # aws update-function-code
  cmd = shlex.split(f'aws lambda update-function-code --function-name {sys.argv[1]} --zip-file fileb://function.zip')
  ret = subprocess.run(cmd, capture_output=True)
  if ret.returncode != 0:
    print(ret.stderr.decode('utf-8'))
  else:
    print('Updated lambda function')

  # remove zip
  os.remove('function.zip')