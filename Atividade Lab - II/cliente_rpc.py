import rpyc

HOST = "127.0.0.1"
PORT = 65431

conn = rpyc.connect(HOST, PORT);
    
print(f"Conectando ao servidor em {HOST}:{PORT}...")
    
horario = conn.root.obter_horario()
print(f"Horário recebido: {horario}")
conn.close()