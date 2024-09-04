import socket

#Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Vinculando o socket ao endereço e porta 
server_socket.bind(("127.0.0.1",12345))

#Executando por conexões
server_socket.listen(5)
print(f"Servidor escutando na porta...")

#Aceitando conexões de clientes
while True:
    conn , addr = server_socket.accept()

    print(f"Conectado por {addr}")

    #Recebendo mensagem do cliente
    data = conn.recv(1024)
    print(f"Mensagem recebida: {data.decode()}")

    #Respondendo ao  cliente
    conn.sendall(b"Mensagem recebida pelo servidor")
    conn.close()
