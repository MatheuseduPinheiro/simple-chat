import socket 

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ConectanDO Servidor 

cliente_socket.connect(('127.0.0.1',12345))

#Enviando uma mensagem para o servidor

mensagem = str(input("Digite uma mensagem : "))

cliente_socket.sendAll()(mensagem.encode)

#Recebendo Resposta 
data = cliente_socket.recv(1024)
print(f"Resposta do Servidor: {data.decode}")
cliente_socket.close()

