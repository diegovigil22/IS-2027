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

# Creamos un socket UDP y añadimos un timeout.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.1)

# Pedimos y enviamos mensajes hasta que se escriba FIN.
while True:
    mensaje = input("Escribe un mensaje (FIN para terminar): ")

    if mensaje == "FIN":
        break

    mensaje_numerado = str(contador) + ": " + mensaje
    s.sendto(mensaje_numerado.encode("utf8"), (ip, puerto))

    try:
        datos, origen = s.recvfrom(1024)
        respuesta = datos.decode("utf8")

        if respuesta == "OK":
            print("Recibida confirmación")
        else:
            print("Recibido datagrama no esperado")

    except socket.timeout:
        print("ERROR. El datagrama de confirmación no llega")

    contador += 1

s.close()

