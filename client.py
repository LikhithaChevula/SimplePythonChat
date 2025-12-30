from encodings import utf_8
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 8080))


done=False
while not done:
    client.send(input("Message:").encode('utf-8'))
    msg=client.recv(1024).decode('utf-8')
    if msg == 'exit':
        done = True
    else:
        print('Received from server:', msg)

client.close()
