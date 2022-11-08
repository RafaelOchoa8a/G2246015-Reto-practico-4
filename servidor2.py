import socket
from datetime import datetime
import os
import platform
host = "localhost"
port = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("El servidor espera de conexiones...")
active, addr = server.accept()

while True:
    recibido = active.recv(1024).decode(encoding="ascii",errors="ignore")
    print("Cliente: ", recibido)
    if recibido == "date":
        enviar = str(datetime.now())
        active.send(enviar.encode(encoding="ascii",errors="ignore"))
    if recibido == "os":
        enviar = str(platform.system() + " " + platform.release() + ", " + platform.processor()) 
        active.send(enviar.encode(encoding="ascii",errors="ignore"))
    if recibido == "ls":
        enviar = str(os.listdir())
        active.send(enviar.encode(encoding="ascii",errors="ignore"))
       
        
active.close()