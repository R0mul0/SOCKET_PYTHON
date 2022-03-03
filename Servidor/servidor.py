import socket
import sys
import threading

def TrataSensor(conn):
    while True:
        data = conn.recv(1000)
        if not data:
            break
        else:
            print('recebi ', len(data), ' bytes')
            print(data)

    conn.close()    
    print('O cliente', conn, 'encerrou')

HOST = '192.168.0.20'
PORTA= 2048
  

print('Servidor Ativo')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORTA))


s.listen(5)

print('aguardando conexoes em ', PORTA)

while True:
    conn, addr = s.accept()
    print('recebi uma conexao de ', addr)
    TrataSensor(conn) 
    print('o cliente encerrou')
    conn.close()
    print('o servidor encerrou')
    s.close()
