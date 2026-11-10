import socket, time, sys

HOST, PORT = '127.0.0.2', 5002
INTERVALO = 3

nid = sys.argv[1] if len(sys.argv) > 1 else input('ID do nó: ').strip()

with socket.socket() as s:
    s.connect((HOST, PORT))
    print(f'Worker {nid} conectado ao monitor. Enviando PING a cada {INTERVALO}s (Ctrl+C para sair).')
    try:
        while True:
            s.sendall(f'PING {nid}'.encode())
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print(f'\nWorker {nid} encerrado.')
    except (BrokenPipeError, ConnectionResetError, OSError) as e:
        print(f'\nWorker {nid}: conexão perdida ({e}).')
