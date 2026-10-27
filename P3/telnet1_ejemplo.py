import getpass
import telnetlib

HOST = "localhost"
user = input("Usuario remoto: ")
password = getpass.getpass("Contraseña: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode("utf8") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("utf8") + b"\n")

tn.write(b"ls /home\n")
tn.write(b"exit\n")

print(tn.read_all().decode("utf8"))

tn.close()