import socket

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta 
server_socket.bind(("127.0.0.1", 12345))

# Executando por conexões
server_socket.listen(5)
print("Servidor escutando na porta 12345...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conectado por {addr}")

    try:
        while True:
            # Recebendo mensagem do cliente
            data = conn.recv(1024)
            if not data:
                print(f"Desconexão detectada para {addr}")
                break
            print(f"Mensagem recebida do {addr}: {data.decode()}")

            # Respondendo ao cliente
            conn.sendall(b"Mensagem recebida pelo servidor")
    except Exception as e:
        print(f"Erro durante a comunicação: {e}")
    finally:
        # Fechando a conexão com o cliente
        conn.close()
