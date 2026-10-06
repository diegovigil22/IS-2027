import socket

# Sustituye esta dirección por el broadcast de tu MV.
# broadcast = "192.168.1.255"
broadcast = "172.18.255.255"
puerto = 12345

# Creamos el socket UDP y activamos broadcast.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Limitamos el tiempo de espera durante la búsqueda.
s.settimeout(2)
primer_servidor = None

# Buscamos servidores en la subred.
s.sendto("BUSCANDO HOLA".encode("utf8"), (broadcast, puerto))
print("Buscando servidores...")

while True:
    try:
        datos, origen = s.recvfrom(1024)
        respuesta = datos.decode("utf8")

        if respuesta == "IMPLEMENTO HOLA":
            print("Servidor encontrado:", origen[0])

            # Guardamos solo la IP del primero que responde.
            if primer_servidor is None:
                primer_servidor = origen[0]

    except socket.timeout:
        break

# Probamos el servicio del primer servidor encontrado.
if primer_servidor is None:
    print("No se ha encontrado ningún servidor")
else:
    print("Probando el servidor:", primer_servidor)

    # En esta fase no usamos timeout.
    s.settimeout(None)

    s.sendto("HOLA".encode("utf8"), (primer_servidor, puerto))

    datos, origen = s.recvfrom(1024)
    respuesta = datos.decode("utf8")

    print("Respuesta del servidor:", respuesta)

s.close()