import socket, threading

HOST, PORT = '127.0.0.2', 5000
clientes = []

def broadcast(msg, remetente=None):
    for c in clientes:
        if c is not remetente:
            try:
                c.sendall(msg)
            except:
                pass

def atender(conn, addr):
    nome = conn.recv(1024).decode()
    clientes.append(conn)
    print(f'{addr} ({nome}) conectado')
    try:
        while True:
            dados = conn.recv(1024)
            if not dados:
                break
            texto = dados.decode()
            print(f'{nome} ({addr}): {texto}')
            broadcast(f'[{nome}] {texto}'.encode(), remetente=conn)
    except:
        pass
    finally:
        clientes.remove(conn)
        conn.close()
        print(f'{nome} ({addr}) desconectado')

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f'Servidor ativo em {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        threading.Thread(target=atender, args=(conn, addr), daemon=True).start()
