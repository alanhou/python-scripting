import socket

host_name  = socket.gethostname()
port = 5000
s_socket = socket.socket()
s_socket.bind((host_name, port))
s_socket.listen(2)

conn, address = s_socket.accept()
print("Connection from: " + str(address))

while True:
        recv_data = conn.recv(1024).decode()
        if not recv_data:
                break
        print("from connected user: " + str(recv_data))
        recv_data = input(' -> ')
        conn.send(recv_data.encode())

conn.close()
