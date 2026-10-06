import socket
import sys
# import time

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

    # time.sleep(1)

    continuar = True

    while continuar:
        mensaje = sd.recv(80)
        mensaje = mensaje.decode("utf8")

        if mensaje == "":
            print("El cliente ha cerrado la conexión")
            sd.close()
            continuar = False

        else:
            linea = mensaje[:-2]
            print("Recibido mensaje:", linea)

            linea = linea[::-1]

            sd.sendall((linea + "\r\n").encode("utf8"))