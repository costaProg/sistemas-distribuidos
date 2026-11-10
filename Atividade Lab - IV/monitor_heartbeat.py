import socket, threading, time, sys

HOST, PORT = '127.0.0.2', 5002
TIMEOUT = 8
INTERVALO_CHECAGEM = 1

nodos = {}
lock = threading.Lock()


def nome_exibicao(nid):
    return nid if nid.startswith('Worker_') else f'Worker_{nid}'


def checar():
    while True:
        time.sleep(INTERVALO_CHECAGEM)
        agora = time.time()
        offline = []
        with lock:
            for nid, ultimo in list(nodos.items()):
                if agora - ultimo > TIMEOUT:
                    offline.append(nid)
                    del nodos[nid]
        for nid in offline:
            print(f'[ALERTA] O Nó {nome_exibicao(nid)} está OFFLINE!')


def atender(conn, addr):
    try:
        while True:
            dados = conn.recv(1024)
            if not dados:
                break
            msg = dados.decode().strip()
            partes = msg.split()
            if len(partes) == 2 and partes[0] == 'PING':
                nid = partes[1]
                with lock:
                    novo = nid not in nodos
                    nodos[nid] = time.time()
                if novo:
                    print(f'[NOVO] Nó {nome_exibicao(nid)} registrado ({addr})')
                else:
                    print(f'[HB] {nome_exibicao(nid)} -> PING OK')
            else:
                print(f'[?] Mensagem inválida de {addr}: {msg}')
    except Exception:
        pass
    finally:
        conn.close()


threading.Thread(target=checar, daemon=True).start()

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f'Monitor de Heartbeat ativo em {HOST}:{PORT} (timeout={TIMEOUT}s)')
    while True:
        conn, addr = s.accept()
        threading.Thread(target=atender, args=(conn, addr), daemon=True).start()
