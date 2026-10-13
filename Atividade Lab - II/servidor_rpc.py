import rpyc
from datetime import datetime

class HorarioService(rpyc.Service):
    
    def exposed_obter_horario(self):
        return datetime.now().strftime("%H:%M:%S")


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 65431
    
    print(f"Servidor RPyC aguardando conexões em {HOST}:{PORT}...")
    
    server = rpyc.ThreadedServer(
        service=HorarioService,
        hostname=HOST,
        port=PORT,
    )
    
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário.")