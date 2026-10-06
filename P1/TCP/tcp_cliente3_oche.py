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

mensajes = ["HOLA", "UNO", "PYTHON"]

for mensaje in mensajes:
    print("Enviando:", mensaje)

    s.sendall((mensaje + "\r\n").encode("utf8"))

    respuesta = s.recv(80)
    respuesta = respuesta.decode("utf8")

    print("Respuesta:", respuesta[:-2])

s.close()