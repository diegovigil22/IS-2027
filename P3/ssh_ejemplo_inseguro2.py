import getpass
import paramiko
import time

password = getpass.getpass("Contraseña de Ubuntu: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

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