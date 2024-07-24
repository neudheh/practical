import socket

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 12345))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()
print(f"You are connected to {addr}! Say hi!")

while True:
    # sends a message
    message = input("Send a message to the client (send END to end the chat):")
    message = message.encode() + b'\n'
    chat_socket.sendall(message)
    # waits for clients message
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)

    # end the program
    if data == b'END\n':
        break
    else:
        print(f"Client says: {data.decode()}")

listen_socket.close()
chat_socket.close()