import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("A conexao falhou !!!")
        print("Erro: {}".format(erro))
        sys.exit()

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a Porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na Porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as erro:
        print("Não foi possivel conectar no Host " + HostAlvo + " - Potar: " + PortaAlvo)
        print("Erro: {}".format(erro))
        sys.exit()
if __name__ == "__main__":
    main()