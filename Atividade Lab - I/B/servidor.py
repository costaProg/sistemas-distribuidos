import socket
import threading
from datetime import datetime

def atende_cliente(conn):
    data = conn.recv(1024)
    if data:
        texto = data.decode("utf-8")
        invertido = texto[::-1]
        conn.sendall(invertido.encode("utf-8"))
    conn.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("127.0.0.1", 8001))
servidor.listen(5)
print("Servidor aguardando...")

while True:
    conn, addr = servidor.accept()
    threading.Thread(target=atende_cliente, args=(conn,)).start()
