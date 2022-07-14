import socket

dominio = input("informe o holts:")

texto = input("informe o Word list para DNS")

with open(texto) as arquivo:
    nomes = arquivo.readline()

for nome in nomes:
    DNS = nome.strip("\n" + "." + dominio)
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass