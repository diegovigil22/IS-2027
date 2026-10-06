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
s.connect((ip, puerto))

# Pedimos y enviamos mensajes hasta que se escriba FIN.
while True:
    mensaje = input("Escribe un mensaje (FIN para terminar): ")

    if mensaje == "FIN":
        break

    mensaje_numerado = str(contador) + ": " + mensaje
    confirmado = False
    timeout = 0.1

    while not confirmado and timeout <= 2:
        s.settimeout(timeout)

        print("Enviando: " + mensaje_numerado)
        print("Tiempo de espera: " + str(timeout) + " segundos")

        s.send(mensaje_numerado.encode("utf8"))

        try:
            datos = s.recv(1024)
            respuesta = datos.decode("utf8")

            if respuesta == "OK":
                print("Recibida confirmación")
                confirmado = True
            else:
                print("Recibido datagrama no esperado")

        except socket.timeout:
            print("ERROR. El datagrama de confirmación no llega")
            timeout *= 2

    if not confirmado:
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        break

    contador += 1

s.close()

