import socket
host = "localhost"
port = 6666

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((host,port))
print("Inicializando el cliente...")

while True:
    enviar = input("Cliente: ")
    socket1.send(enviar.encode(encoding="ascii",errors="ignore"))
    recibido = socket1.recv(1024)
    print("Servidor: ", recibido.decode(encoding="ascii",errors="ignore"))

socket1.close()