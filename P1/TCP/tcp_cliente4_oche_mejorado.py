import socket
import sys

def recibe_mensaje(sock):
    buffer = []

    while True:
        byte = sock.recv(1)

        if byte == b"":
            return b""

        buffer.append(byte)

        if len(buffer) >= 2:
            if buffer[-2] == b"\r" and buffer[-1] == b"\n":
                return b"".join(buffer)

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

for i in range(3):
    respuesta = recibe_mensaje(s)
    respuesta = respuesta.decode("utf8")

    print(repr(respuesta))

s.close()