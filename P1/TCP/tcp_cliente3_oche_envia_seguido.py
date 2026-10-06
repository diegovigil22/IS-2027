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

# Primero enviar los tres mensajes
for mensaje in mensajes:
    print("Enviando:", mensaje)
    s.sendall((mensaje + "\r\n").encode("utf8"))

# Después intentar recibir tres respuestas
for i in range(3):
    respuesta = s.recv(80)
    respuesta = respuesta.decode("utf8")

    print(repr(respuesta))

s.close()