import socket
import json

"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANDREI OROZCO
"""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client socket created")

host = 'localhost'
port = 5433

machine_ID = 'm1'
server_addr = 0

"""
IN THIS FUNCTION THE CLIENT WILL SELECT THEIR DESIRED
CURSE OF ACTION AS DISCUSED IN THE COMMENTS IN MAIN
"""
def client_Main_Menu():
    option = True
    while option:
        print("To visualize the group manipulation menu press 1")
        print("To visualize the math operations menu press 2")


def client_Comunication():
    print("Will now attemp comunication with server")
    """
    SENDING SERVER OUT MACHINE ID SO THAT WE CAN BE IDENTIFIED
    """
    client_socket.sendto(machine_ID.encode(), (host, 5432))

    """
    REVIEVING CONFIRMATION MESSAGE THAT SERVER GOT THE MACHINE ID
    """
    confirmation_message, server_addr = client_socket.recvfrom(4096)
    confirmation_message = confirmation_message.decode()
    print(confirmation_message)

    """
    AT THIS POINT THE USER MUST DECIDE WHAT TO DO
    NOTHING AND WAIT
    SELECT TO MANIPULATE THE GROUP MATRIX
    SELECT TO DO A MATH OPERATION
    """
    client_Main_Menu()

def main():
    client_Comunication()

if __name__ == "__main__":
    main()
