import socket
import sys

ip = "localhost"
puerto = 9999

# Si se indican argumentos, usamos esos valores.
if len(sys.argv) > 1:
    ip = sys.argv[1]

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

# Creamos un socket UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Pedimos y enviamos mensajes hasta que se escriba FIN.
while True:
    mensaje = input("Escribe un mensaje (FIN para terminar): ")

    if mensaje == "FIN":
        break

    s.sendto(mensaje.encode("utf8"), (ip, puerto))

s.close()

