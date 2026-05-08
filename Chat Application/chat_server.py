import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

clients = []


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)

            if not message:
                break

            broadcast(message, client_socket)

        except:
            break

    if client_socket in clients:
        clients.remove(client_socket)

    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Chat server started...")
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        print(f"New connection from {address}")

        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


start_server()