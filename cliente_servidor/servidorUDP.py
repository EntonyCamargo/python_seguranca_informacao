import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socke Criando com sucessso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nservidor: Olaaaa cliente '

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem........')
        s.sendto(dados + (mensagem.encode()), end)