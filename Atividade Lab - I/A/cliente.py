import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 65430))

cliente.sendall("Qual o horário?".encode())
print("Horário:", cliente.recv(1024).decode())
cliente.close()
