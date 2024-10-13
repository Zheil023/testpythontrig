import socket

# Set the port and address
HOST = 'localhost'  # Address (usually 'localhost' for local connections)
PORT = 65432        # Change the port number if needed

def create_socket():
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the specified host and port
        sock.connect((HOST, PORT))
        return sock
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None
