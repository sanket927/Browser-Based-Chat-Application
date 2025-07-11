import socket
import threading

# Set up the server
host = '127.0.0.1'  # localhost
port = 5000         # any unused port



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"🔌 Server is running on {host}:{port}")
conn, addr = server.accept()
print(f"✅ Client connected from {addr}")

# Receive messages from client
def receive():
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"\nClient: {message}")
        except:
            print("❌ Connection lost.")
            break

# Send messages to client
def send():
    while True:
        message = input("You: ")
        conn.send(message.encode())

# Run send and receive in parallel
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
