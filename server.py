import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Server is listening on port 8080 ...")

client, addr = server_socket.accept()
print(f"Connection from {addr} has been established!")

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'exit':
        done = True
    else:
        print(f"Received: {msg}")
        client.send(input("Message:").encode('utf-8'))

client.close()
server_socket.close()