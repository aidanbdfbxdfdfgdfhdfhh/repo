import socket

HOST = "127.0.0.1"   # localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Server running on {HOST}:{PORT}")

conn, addr = server.accept()

print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)

    if not data:
        break

    message = data.decode()

    print("Client said:", message)

    reply = input("Reply: ")

    conn.send(reply.encode())

conn.close()