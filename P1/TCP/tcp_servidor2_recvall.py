import socket
import sys

def recvall(sock, cantidad):
    datos = b""

    while len(datos) < cantidad:
        recibidos = sock.recv(cantidad - len(datos))

        if recibidos == b"":
            return b""

        datos += recibidos

    return datos

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

    continuar = True

    while continuar:
        # recvall()
        datos = recvall(sd, 5)
        datos = datos.decode("ascii")

        if datos == "":
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False

        elif datos == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False

        else:
            print("Recibido mensaje:", datos)