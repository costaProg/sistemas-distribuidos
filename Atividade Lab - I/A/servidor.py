import socket
import threading
from datetime import datetime

def atende_cliente(conn):
    data = conn.recv(1024)
    if data:
        conn.sendall(datetime.now().strftime("%H:%M:%S").encode())
    conn.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("127.0.0.1", 65430))
servidor.listen(5)
print("Servidor aguardando...")

while True:
    conn, addr = servidor.accept()
    threading.Thread(target=atende_cliente, args=(conn,)).start()
