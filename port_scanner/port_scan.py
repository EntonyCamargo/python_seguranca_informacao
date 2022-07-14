import socket

host = str(input("informe o ip alvo: "))

portas = [21, 22, 23, 25, 80, 110,]
print("Portas abertas:")
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    codigoRetorno = sock.connect_ex((host, porta))
    sock.close()
    if codigoRetorno == 0:
        print(porta)