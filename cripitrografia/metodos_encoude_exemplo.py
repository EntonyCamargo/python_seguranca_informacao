import base64

text_cod = str(input("Escreva o texto a ser Codificado:"))
encerrar = "SAIR"

encoded = (base64.b64encode(text_cod.encode('ascii')))
encoded_ascii = encoded.decode('ascii')

pergunta = input("Se deseja Mostrar o texto codificado escreva \"CODIFICADO\" \n " 
                 " agora, se deseaja escerrar o programa escreva \"SAIR\"\n: ").upper()

if pergunta == "CODIFICADO":
    print(encoded)
elif pergunta == "SAIR":
    print(exit())