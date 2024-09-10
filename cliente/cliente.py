import socket

def parametrosConexao(ip, porta):
    """ Verifica a conexão com o servidor e retorna uma mensagem adequada. """
    return f"Cliente se conectou à porta {porta}" if ip == '127.0.0.1' and porta == 12345 else f"Nenhum servidor detectado na porta {porta}"

# Criando um socket TCP/IP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectando ao Servidor
    cliente_socket.connect(('127.0.0.1', 12345))
    
    # Verificando a conexão
    print(parametrosConexao('127.0.0.1', 12345))
    
    while True:
        # Enviando uma mensagem para o servidor
        mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()
        
        if mensagem.lower() == 'sair':
            print("Encerrando a conexão...")
            break
        
        if mensagem == '':
            print("Mensagem não pode ser vazia. Tente novamente.")
            continue
        
        cliente_socket.sendall(mensagem.encode())

        # Recebendo Resposta
        data = cliente_socket.recv(1024)
        print(f"Resposta do Servidor: {data.decode()}")
        
except ConnectionError as e:
    print(f"Erro de conexão: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    # Fechando a conexão
    cliente_socket.close()
    print("Conexão fechada.")
