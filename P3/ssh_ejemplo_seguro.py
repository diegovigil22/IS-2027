import getpass
import paramiko
import time
import base64

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

stdin, stdout, stderr = client.exec_command("ls")

for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()