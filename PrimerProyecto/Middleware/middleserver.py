import socket
import zmq
import json


"""This is for the UDP protocol"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Middleware socket created')
host = 'localhost'
port = 5432

"""This is for the TCP protocol"""
context = zmq.Context()
socket_tcp = context.socket(zmq.REQ)
socket_tcp.connect("tcp://127.0.0.1:5555")

"""UDP socket bind"""
server_socket.bind((host, port))
print('Middleware socket connected to', host)

"""Default Messages"""
confirmationMessage = 'Data recieved in middleserver'



while True:
    """ Recieves data and sends confirmation UDP"""
    data, addr = server_socket.recvfrom(4096)
    if data:
        """UDP"""
        print('Data Recieved Succesfully')
        data = json.loads(data.decode())
        arrayData = data.get("data")
        option = arrayData[0]
        number1 = arrayData[1]
        number2 = arrayData[2]
        try:
            """UDP"""
            server_socket.sendto(confirmationMessage.encode(), addr)
            res, adr = server_socket.recvfrom(4096)
            """TCP"""
            socket_tcp.send_json(data)
            """Getting result from server & sending to client"""
            """TCP"""
            confirmation = socket_tcp.recv()
            confirmation = confirmation.decode()
            print(confirmation)
            """Asking for the result to server"""
            result = '0'
            socket_tcp.send_string(result)
            print('Sending ', result)
            """Recieving result"""
            result = socket_tcp.recv()
            print('From server: ', result.decode())
            """UDP"""
            """Sending result to client"""
            server_socket.sendto(result, addr)
            print('')
        except Exception as e:
            print(e)
