import socket
import json
import sys

HOST = '0.0.0.0'
PORT = 9201

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as ex:
  sys.stderr.write("[ERROR] {}".format(ex.message))
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except socket.error as ex:
  sys.stderr.write("[ERROR] {}".format(ex.message))
  sys.exit(2)

error_message = {'@message': 'A beautiful and cool error message', '@tags': ['test']}

sock.send(json.dumps(error_message) + "\n")

sock.close()
sys.exit(0)
