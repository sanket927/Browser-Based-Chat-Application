import socket
import threading

# Connect to the server
host = '127.0.0.1'  # server IP
port = 5000         # must match server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print(f"🤝 Connected to server at {host}:{port}")

# Receive messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"\nServer: {message}")
        except:
            print("❌ Connection lost.")
            break

# Send messages to server
def send():
    while True:
        message = input("You: ")
        client.send(message.encode())

# Run send and receive in parallel
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
