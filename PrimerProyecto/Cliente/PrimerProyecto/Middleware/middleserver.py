import socket
import zmq


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


while True:
    """ Recieves Number 1 and sends confirmation UDP"""
    number1, addr = server_socket.recvfrom(4096)
    if number1:
        """UDP"""
        print('First Number Recieved Succesfully')
        number1 = number1.decode()
        server_socket.sendto(number1.encode(), addr)
    """ Recieves Number 2 and sends confirmation UDP"""
    number2, addr = server_socket.recvfrom(4096)
    if number2:
        """UDP"""
        print('Second Number Recieved Succesfully')
        number2 = number2.decode()
        server_socket.sendto(number2.encode(), addr)
    """ Adds numers and sends answer UDP"""
    res, adr = server_socket.recvfrom(4096)
    if number1 and number2:
        """UDP"""
        print('Numbers Recieved Succesfully')
        print(number1 + " " + number2)
        """Sending number 1 and recieving confirmation"""
        try:
            """TCP"""
            socket_tcp.send_string(number1)
            print('Sending ', number1)
            number1 = socket_tcp.recv()
            print('From server: ', number1.decode())
            print('')
        except Exception as e:
            print(e)
        """Sending number 2 and recieving confirmation"""
        try:
            """TCP"""
            socket_tcp.send_string(number2)
            print('Sending ', number2)
            number2 = socket_tcp.recv()
            print('From server: ', number2.decode())
            print('')
        except Exception as e:
            print(e)
        """Getting result"""
        try:
            """TCP"""
            result = '0'
            socket_tcp.send_string(result)
            print('Sending ', result)
            result = socket_tcp.recv()
            print('From server: ', result.decode())
            """UDP"""
            server_socket.sendto(result, addr)
            print('')
        except Exception as e:
            print(e)
