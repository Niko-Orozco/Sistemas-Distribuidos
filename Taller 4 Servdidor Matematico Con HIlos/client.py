import socket 
import time 
import json
import sys



"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANDREI OROZCO
"""

client_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client Socket Created")
host = 'localhost'
port = 5433


def main():
    userControler()


def userControler():
    option = True
    while option: 
        printMenu()
        opt = input('>>>')
        if opt == 'a':
            array_Length = input('How many numbers do you wish to add? ')
            number_Array = []
            for i in range(int(array_Length)):
                number_Array.append(input("Enter a number: "))
            print(number_Array)
            add(opt, number_Array)
        if opt == 's':
            array_Length = input('How many numbers do you wish to subtract? ')
            number_Array = []
            i = 0
            for i in range(int(array_Length)):
                number_Array.append(input("Enter a number: "))
            print(number_Array)
            sub(opt, number_Array)


def printMenu():
    print('-------------Welcome to our Calculator Service-----------')
    print('Press a to add a list of numbers')
    print('Press s to subtract a list of numbers')
    print('Press e to exit')

def add(opt, number_Array):
    array_Data = [opt, number_Array]
    data = json.dumps({"data" : array_Data})
    """Sending the number array and recieving the result"""
    try: 
        client_Socket.sendto(data.encode(), (host,5432))
        print("Data sent")
    except Exception as e:
        print(e)
    """Getting Results"""
    try:
        result, socket = client_Socket.recvfrom(4096)
        result = result.decode()
        print("The result of adding is: ", result)
    except Exception as e:
        print(e)

def sub(opt, number_Array):
    array_Data = [opt, number_Array]
    data = json.dumps({"data" : array_Data})
    """Sending the number array and recieving the result"""
    try:
        client_Socket.sendto(data.encode(), (host, 5432))
        print("Data sent")
    except Exception as e: 
        print(e)
    """Getting Results"""
    try: 
        result, socket = client_Socket.recvfrom(4096)
        result = result.decode()
        print("The result from subtracting is: ", result)
    except Exception as e: 
        print(e)



if __name__ == "__main__":
    main()
