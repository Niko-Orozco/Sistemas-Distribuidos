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
    userControler()


def printMenu():
    print('----- Welcome to our Calculator Service -----')
    print('Press a to add')
    print('Press s to substract')
    print('Press m to multiply')
    print('Press p to power')
    print('Press l for logarithm')
    print('Press e to exit')

def add(number1, number2):
    """Sending number 1 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        client_socket.sendto(number1.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('Confirmation the number arrived at the server: ' + confirmation)
    except Exception as e:
        print(e)

    """Sending number 2 and recieving confirmation"""
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



def userControler():
    option = True
    while option:
        number1 = input('enter the number you wish to add: ')
        number2 = input('enter the number you wish to add: ')
        printMenu()
        opt = input('>>>')
        if opt == 'a':
            add(number1, number2)
        elif opt == 'e':
            client_socket.close()
            print('Client socket closed')
            option = False
        """
        elif opt == 's':

        elif opt == 'm':

        elif opt == 'p':

        elif opt == 'l':
        """



if __name__ == "__main__":
    main()
