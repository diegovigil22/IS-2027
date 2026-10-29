import getpass
import paramiko
import time
import base64
import os
from stat import S_ISDIR

password = getpass.getpass("Contraseña de Ubuntu: ")

client = paramiko.SSHClient()
key = paramiko.Ed25519Key(
    data=base64.b64decode(b"AAAAC3NzaC1lZDI1NTE5AAAAICafE6YOravIwfppIaht1JJbNsc5MEaw3SyypG06zvMQ")
)
client.get_host_keys().add("localhost", "ssh-ed25519", key)

client.connect(
    "localhost",
    username="uo302166",
    password=password
)

print("Conectado!!")

carpeta_remota = input("Carpeta remota que quieres descargar: ")
carpeta_local = "descargas_sftp"

os.makedirs(carpeta_local, exist_ok=True)

sftp = client.open_sftp()
sftp.chdir(carpeta_remota)

listado = sftp.listdir()

for nombre in listado:
    datos = sftp.stat(nombre)

    if not S_ISDIR(datos.st_mode):
        destino = os.path.join(carpeta_local, nombre)
        sftp.get(nombre, destino)
        print("Descargado:", nombre)

sftp.close()
client.close()