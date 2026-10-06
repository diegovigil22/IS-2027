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

f = s.makefile(encoding="utf8", newline="\r\n")

mensajes = ["HOLA", "UNO", "PYTHON"]

# Enviar los tres mensajes seguidos
for mensaje in mensajes:
    print("Enviando:", mensaje)
    s.sendall((mensaje + "\r\n").encode("utf8"))

# Recibir las tres respuestas
for i in range(3):
    respuesta = f.readline()
    print(repr(respuesta))

f.close()
s.close()