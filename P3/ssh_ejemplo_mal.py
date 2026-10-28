import paramiko
import time

client = paramiko.SSHClient()
client.connect(
    "localhost",
    username="uo302166",
    password="clave-mal"
)

print("Conectado!!")

# Ejecutar el comando remoto.
stdin, stdout, stderr = client.exec_command("ls")

# Mostrar su salida.
for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()