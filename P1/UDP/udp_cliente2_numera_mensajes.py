import socket
import sys

ip = "localhost"
puerto = 9999
contador = 1

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

    mensaje_numerado = str(contador) + ": " + mensaje
    s.sendto(mensaje_numerado.encode("utf8"), (ip, puerto))

    contador += 1

s.close()

