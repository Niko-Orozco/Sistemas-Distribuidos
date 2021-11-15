import numpy as np
import socket
import json


"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANREI OROZCO
"""
client_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client Socket Created')
host = 'localhost'
port = 5433

"""
WHAT DOES THE USER NEED?
CREATE, DELETE, ENTER OR EXIT ANY GROUP. ANY USER MAY BE PART OF ANY GROUP
LIST THE EXISTING GROUPS
SEND A MESSAGE TO ANY GROUP
"""
def main():
    machine_ID = 'm1'
    mainController(machine_ID)
    mathController(machine_ID)

def printMathMenu():
    print('----- Welcome to our Calculator Service -----')
    print('Press 1 to add')
    print('Press 2 to subtract')
    print('Press 3 to multiply')
    print('Press 4 to divide')
    print('Press 5 to power')
    print('Press 6 for logarithm')
    print('Press 7 to exit')
    print("\n")



def add(opt, number1, number2, machine_ID):
    data_Set = {"option" : opt, "number1" : number1, "number2": number2, "machine": machine_ID}
    data = json.dumps(data_Set)
    try:
        client_socket.sendto(data.encode(), (host,5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print("From group server: ", confirmation)
    except Exception as e:
        print(e)
        """
        YOU ARE IN THE PROCESS OF MAKING THE ADDING PROCESS FOR THE CLIENTS AND THE SERVERS
        EDITORS NOTE: IDEA-- EVERY TIME A CLIENT CONNECTS WILL SEND A HELLO MESSAGE
        TO THE SERVER SO THAT IT CAN BE IDENTIFIED AND SAVED IN A LIST OF ADDRESSES
        """
"""
THIS FUNCTION CORRESPONDS TO THE CONTROLLER FOR THE MATHEMATICAL OPERATIONS
"""
def mathController(machine_ID):
    option = True
    while option:
        printMathMenu()
        opt = input("Please enter your selection: ")
        if(opt == '1'):
            number1 = input("Please enter the first number for addition")
            number2 = input("Please enter the second number for addition")
            add(opt, number1, number2, machine_ID)

def mainController(machine_ID):
    print('----- Welcome to our Service -----')
    print('Press 1 to redirect to the math controller')
    print('Press 2 to redirect to the user controller')
    opt = input("Please enter your selection: ")
    if(opt == '1'):
        mathController(machine_ID)
    if(opt == '2'):
        userController(machine_ID)







if __name__ == "__main__":
    main()
