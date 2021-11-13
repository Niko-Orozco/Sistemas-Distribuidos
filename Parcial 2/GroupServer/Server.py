import numpy as np
import socket
import json


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Middleware socket created")
host = 'localhost'
port = 5432

server_socket.bind((host, port))
print("Middleware socket connected to: ", localhost)
