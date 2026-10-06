import socket
import sys

def envia_mensaje(sock, mensaje):
    datos = mensaje.encode("utf8")
    cabecera = (str(len(datos)) + "\n").encode("ascii")

    sock.sendall(cabecera + datos)

def recibe_mensaje(f):
    cabecera = f.readline()

    if cabecera == b"":
        return None

    longitud = int(cabecera)
    datos = f.read(longitud)

    if len(datos) < longitud:
        return None

    return datos.decode("utf8")

puerto = 9999

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", puerto))
s.listen(5)

while True:
    print("Esperando un cliente")

    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)

    f = sd.makefile("rb")

    continuar = True

    while continuar:
        mensaje = recibe_mensaje(f)

        if mensaje is None:
            print("Conexión terminada")
            f.close()
            sd.close()
            continuar = False

        else:
            print("Recibido mensaje:", mensaje)

            respuesta = mensaje[::-1]
            envia_mensaje(sd, respuesta)