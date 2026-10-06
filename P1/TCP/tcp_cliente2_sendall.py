import socket
import sys

ip = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    ip = sys.argv[1]

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, puerto))

for i in range(5):
    s.sendall("ABCDE".encode("ascii"))

# for i in range(4):
  #  s.sendall("ABCD".encode("ascii"))

s.sendall("FINAL".encode("ascii"))

s.close()