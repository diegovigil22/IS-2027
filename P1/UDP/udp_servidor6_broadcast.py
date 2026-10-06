import socket

puerto = 12345

# Creamos el socket UDP y activamos broadcast.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Escuchamos en el puerto del servicio.
s.bind(("", puerto))

print("Servidor HOLA esperando mensajes en el puerto", puerto)

while True:
    datos, origen = s.recvfrom(65535)
    mensaje = datos.decode("utf8")

    print("Mensaje recibido:", mensaje)
    print("Enviado desde:", origen)

    if mensaje == "BUSCANDO HOLA":
        respuesta = "IMPLEMENTO HOLA"
        s.sendto(respuesta.encode("utf8"), origen)

    elif mensaje == "HOLA":
        respuesta = "HOLA: " + origen[0]
        s.sendto(respuesta.encode("utf8"), origen)