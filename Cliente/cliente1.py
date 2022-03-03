import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Entre com o IP do servidor:')
IP= input()

print('Entre com a porta do servidor:')
PORTA= int(input())

print('Entre com o IP ou Nome:')
ID= input()

try:
    s.connect((IP, PORTA))
except:
    print('Erro de conexao')

s.send(bytes(ID, 'utf-8'))

while True:
    try:
        line = input()
        if not line:
            print('Linha vazia encerra o programa')
            break
    except:
            print('Programa abortado com CTRL+C')
    data = bytes(line, 'utf-8')
    tam = s.send(data)
           
    print('enviei ',tam, 'bytes')
    print(data)