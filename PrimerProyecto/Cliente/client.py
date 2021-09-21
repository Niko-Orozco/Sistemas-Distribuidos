import zmq
import time
import socket
import sys
"""
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")
"""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client Socket Created')
host = 'localhost'
port = 5433




def main():
    """Sending number 1 and recieving confirmation"""
    number1 = input('enter the number you wish to add: ')
    try:
        print('Client first number: '+ number1)
        client_socket.sendto(number1.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('Confirmation the number arrived at the server: ' + confirmation)
    except Exception as e:
        print(e)

    """Sending number 2 and recieving confirmation"""
    number2 = input('enter the number you wish to add: ')
    try:
        print('Client second number: '+ number2)
        client_socket.sendto(number2.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('Confirmation the number arrived at the server: ' + confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of adding: ' + result)
    except Exception as e:
        print(e)

    finally:
        print('Client Closing Socket')
        client_socket.close()

if __name__ == "__main__":
    main()

    """
    msg = input('enter your msg here: ')
    socket.send_string(msg)
    print('Sending ', msg)
    print('From server: ', socket.recv())
    print('')
    """
