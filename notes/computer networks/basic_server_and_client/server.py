import socket

# creates a socket to listen for connection, and binds it to the ip
listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 12345))
listen_socket.listen()

# creates a new socket for communication when a connection is made
new_socket, addr = listen_socket.accept()
print(f"Connected to {str(addr)}")
# sends a message and closes
new_socket.sendall(b'Hello from the server!\n')
new_socket.close()
listen_socket.close()