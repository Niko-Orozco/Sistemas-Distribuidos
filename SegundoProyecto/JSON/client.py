import zmq
import time
import sys
import json


"""This is for the TCP protocol"""
context = zmq.Context()
socket_tcp = context.socket(zmq.REQ)
socket_tcp.connect("tcp://127.0.0.1:5555")


def main():
    userControler()


def printMenu():
    print('----- Welcome to our Calculator Service -----')
    print('Press a to add')
    print('Press s to subtract')
    print('Press m to multiply')
    print('Press d to divide')
    print('Press p to power')
    print('Press l for logarithm')
    print('Press e to exit')

def add(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of adding: ' + result.decode())
    except Exception as e:
        print(e)

def subtract(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of substracting: ' + result.decode())
    except Exception as e:
        print(e)

def multiply(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of multiplying: ' + result.decode())
    except Exception as e:
        print(e)

def divide(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of dividing: ' + result.decode())
    except Exception as e:
        print(e)

def power(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of exponentiation: ' + result.decode())
    except Exception as e:
        print(e)

def logarithm(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = {
      "data": arrayData,
    }
    jsondata = json.dumps(data)
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        socket_tcp.send_json(jsondata)
        confirmation = socket_tcp.recv()
        confirmation = confirmation.decode()
        print(confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        result = "0"
        socket_tcp.send_string(result)
        result = socket_tcp.recv()
        print('The result of logarithm: ' + result.decode())
    except Exception as e:
        print(e)

def userControler():
    option = True
    while option:
        printMenu()
        opt = input('>>>')
        if opt == 'a':
            number1 = input('Please enter the first number for addition: ')
            number2 = input('Please enter the second number for addition: ')
            add(opt, number1, number2)
        elif opt == 's':
            number1 = input('Please enter the first number for subtraction: ')
            number2 = input('Please enter the second number for subtraction: ')
            subtract(opt, number1, number2)
        elif opt == 'm':
            number1 = input('Please enter the first number for multiplication: ')
            number2 = input('Please enter the second number for multiplication: ')
            multiply(opt, number1, number2)
        elif opt == 'd':
            number1 = input('Please enter the first number for division: ')
            number2 = input('Please enter the second number for division: ')
            divide(opt, number1, number2)
        elif opt == 'p':
            number1 = input('Please enter the base: ')
            number2 = input('Please enter the power/exponent: ')
            power(opt, number1, number2)
        elif opt == 'l':
            number1 = input('Please enter the base: ')
            number2 = input('Please enter the number: ')
            logarithm(opt, number1, number2)
        elif opt == 'e':
            client_socket.close()
            print('Client socket closed')
            option = False
        else:
            print('Please enter a valid option')
            sleep(2)
            userControler()




if __name__ == "__main__":
    main()
