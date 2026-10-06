import socket
import sys

puerto = 9999

# Si se indica un puerto por línea de comandos, usamos ese.
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

# Creamos un socket UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociamos el socket al puerto elegido.
s.bind(("", puerto))

print("Servidor UDP esperando mensajes en el puerto", puerto)

# Recibimos mensajes en un bucle infinito.
while True:
    datos, origen = s.recvfrom(65535)

    mensaje = datos.decode("utf8")

    print("Mensaje recibido:", mensaje)
    print("Enviado desde:", origen)