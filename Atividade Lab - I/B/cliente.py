import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 8001))

mensagem = "Olá, Mundo Distribuído"
cliente.sendall(mensagem.encode("utf-8"))
resposta = cliente.recv(1024)
print("Mensagem Invertida:", resposta.decode("utf-8"))
cliente.close()
