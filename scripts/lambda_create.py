#! /usr/bin/python3
import subprocess
import sys
import os
from zipfile import ZipFile

ret = subprocess.run(['aws', 'iam', 'get-role', \
                            '--role-name', sys.argv[1], \
                            '--query', 'Role.[Arn]', \
                            '--output', 'text'], \
                            capture_output=True)
arn = ret.stdout.decode('utf-8').strip('\n')

folder_path = os.path.join('src', 'lambda')
with ZipFile('function.zip', 'w') as archive:  
  for filename in os.listdir(folder_path):
    archive.write(os.path.join(folder_path, filename), filename)

ret = subprocess.run(['aws', 'lambda', 'create-function', \
                           '--function-name', sys.argv[2], \
                           '--role', arn, \
                           '--zip-file', 'fileb://function.zip', \
                           '--runtime', 'nodejs16.x', \
                           '--handler', 'index.handler'], \
                           capture_output=True)
                           

os.remove('function.zip')