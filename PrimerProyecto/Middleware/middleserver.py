import socket
import zmq



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Middleware socket created')
host = 'localhost'
port = 5432

server_socket.bind((host, port))
print('Middleware socket connected to', host)

confirmationMessage = 'The client number is: '
resultMessage = 'The result is: '

while True:
    """ Recieves Number 1 and sends confirmation"""
    number1, addr = server_socket.recvfrom(4096)
    if number1:
        print('First Number Recieved Succesfully')
        number1 = number1.decode()
        server_socket.sendto(number1.encode(), addr)
    """ Recieves Number 2 and sends confirmation"""
    number2, addr = server_socket.recvfrom(4096)
    if number2:
        print('Second Number Recieved Succesfully')
        number2 = number2.decode()
        server_socket.sendto(number2.encode(), addr)
    """ Adds numers and sends answer"""
    res, adr = server_socket.recvfrom(4096)
    if number1 and number2:
        print('Numbers Recieved Succesfully')
        print(number1 + " " + number2)
        num1 = (int(number1))
        num2 = (int(number2))
        result = num1 + num2
        res.decode()
        res = (str(result))
        print('result ' + res)

        server_socket.sendto(res.encode(), addr)
