import telnetlib
import time

HOST = "localhost"
user = "uo302166"
password = "Gildina985"

tn = telnetlib.Telnet(HOST)

# Iniciar sesión.
tn.read_until(b"login: ")
tn.write(user.encode("utf8") + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode("utf8") + b"\n")

# Descartar la bienvenida y esperar al prompt.
tn.read_until(b"$")

# Consultar los procesos en ejecución.
tn.write(b"ps -efww\n")
respuesta = tn.read_until(b"$")

if b"udp_servidor3_con_ok.py" in respuesta:
    print("El servidor ya está en ejecución")
else:
    # Arrancar el servidor y mantenerlo tras cerrar Telnet.
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n")
    time.sleep(1)

# Terminar la sesión y mostrar la respuesta pendiente.
tn.write(b"exit\n")
print(tn.read_all().decode("utf8"))

tn.close()