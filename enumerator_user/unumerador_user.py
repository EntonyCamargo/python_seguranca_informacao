import socket

ip_alvo = str(input("Infome o ip alvo: "))

porta_alvo = str(input("Infome a porta de EMAIL alvo: "))

usuarios = ['Daniel', 'Pedro', 'root']

for user in usuarios:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_alvo, porta_alvo))
    sock.recv(1024)
    sock.send('VRFY' + user + '\n')
    resposta = sock.recv(1024)
    sock.close()
    if 252 in resposta:
        print(user + "-> Valido!")
    elif 550 in resposta:
        print(user + "-> Usuario nao encontrado!")
    elif 503 in resposta:
        print('Servidor requer autenticacao')
        break
    elif 500 in resposta:
        print("Comandi VRFY nao suportado pelo servidor")
        break
    else:
        print("Resposta do servidor:", resposta)