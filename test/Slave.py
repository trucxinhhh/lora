import socket
from urllib import request, parse
from seeed_dht import DHT
import time
# Define the IP address and port to listen on
server_ip = "0.0.0.0"  # Listen on all available network interfaces
port = 20000  # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_ip, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server is listening on {server_ip}:{port}")

sensor = DHT('11', 12)

while True:
    humidity, temperature = sensor.read() 
    print('Temperature {}C, Humidity {}%'.format(temperature, humidity))

    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    data_to_send=str(temperature)+str(humidity)
    client_socket.sendall(data_to_send.encode())
    
    print("success")
    client_socket.close()