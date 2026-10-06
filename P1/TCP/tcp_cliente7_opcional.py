import socket
import sys
import struct

def envia_mensaje(sock, mensaje):
    datos = mensaje.encode("utf8")
    cabecera = struct.pack(">H", len(datos))

    sock.sendall(cabecera + datos)

def recibe_mensaje(f):
    cabecera = f.read(2)

    if len(cabecera) < 2:
        return None

    longitud = struct.unpack(">H", cabecera)[0]
    datos = f.read(longitud)

    if len(datos) < longitud:
        return None

    return datos.decode("utf8")

ip = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    ip = sys.argv[1]

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, puerto))

f = s.makefile("rb")

mensajes = ["HOLA", "UNO", "PYTHON"]

for mensaje in mensajes:
    print("Enviando:", mensaje)
    envia_mensaje(s, mensaje)

for i in range(len(mensajes)):
    respuesta = recibe_mensaje(f)

    if respuesta is None:
        print("Conexión terminada antes de recibir todas las respuestas")
        break

    print("Respuesta:", repr(respuesta))

f.close()
s.close()