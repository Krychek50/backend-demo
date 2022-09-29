#! /usr/bin/python3
import subprocess
import shlex
import sys
import os
import json

if __name__ == '__main__':
  # aws invoke
  cmd = shlex.split(f'aws lambda invoke --function-name {sys.argv[1]} outputfile.txt')
  ret = subprocess.run(cmd, capture_output=True)
  
  data = json.loads(ret.stdout)
  os.remove('outputfile.txt')

  # test response
  print(data)
  if data['StatusCode'] != 200 or 'FunctionError' in data:
    sys.exit(os.EX_SOFTWARE)