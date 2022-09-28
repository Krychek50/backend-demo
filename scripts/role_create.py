#! /usr/bin/python3
import subprocess
import sys

ret = subprocess.run(['aws', 'iam', 'create-role', \
                                    '--role-name', sys.argv[1], \
                                    '--assume-role-policy-document', 'file://roles/trust-policy.json'], \
                                    capture_output=True)
print(ret.returncode)
ret = subprocess.run(['aws', 'iam', 'attach-role-policy', \
                                    '--role-name', sys.argv[1], \
                                    '--policy-arn', 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'], \
                                    capture_output=True)
print(ret.returncode)