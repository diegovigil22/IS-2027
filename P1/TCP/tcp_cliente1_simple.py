import socket
import sys

ip = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    ip = sys.argv[1]

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

# Crear el socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
s.connect((ip, puerto))

# Enviar cinco mensajes
for i in range(5):
    s.send("ABCDE".encode("ascii"))

# Indicar que hemos terminado
s.send("FINAL".encode("ascii"))

# Cerrar la conexión
s.close()