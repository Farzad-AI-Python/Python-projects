import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break


def send_messages(client, username):
    while True:
        message = input("")

        if message.lower() == "exit":
            client.close()
            break

        full_message = f"{username}: {message}"
        client.send(full_message.encode("utf-8"))


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    username = input("Enter your username: ")

    print("Connected to chat server.")
    print("Type 'exit' to leave the chat.")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client, username))
    send_thread.start()


start_client()