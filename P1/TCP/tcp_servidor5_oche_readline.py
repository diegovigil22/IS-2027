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

    f = sd.makefile(encoding="utf8", newline="\r\n")

    continuar = True

    while continuar:
        mensaje = f.readline()

        if mensaje == "":
            print("El cliente ha cerrado la conexión")
            f.close()
            sd.close()
            continuar = False

        else:
            linea = mensaje[:-2]
            print("Recibido mensaje:", linea)

            linea = linea[::-1]

            sd.sendall((linea + "\r\n").encode("utf8"))