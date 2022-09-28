#! /usr/bin/python3
import subprocess
import sys
import os
from zipfile import ZipFile

folder_path = os.path.join('src', 'lambda')
with ZipFile('function.zip', 'w') as archive:  
  for filename in os.listdir(folder_path):
    archive.write(os.path.join(folder_path, filename), filename)

ret = subprocess.run(['aws', 'lambda', 'update-function-code', \
                                '--function-name', sys.argv[1], \
                                '--zip-file', 'fileb://function.zip'], \
                                capture_output=True)


os.remove('function.zip')