import socket
import json


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Middleware socket created")
host = 'localhost'
port = 5432

server_socket.bind((host, port))
print("Middleware socket connected to: ", localhost)



def main():
    """
    The matrix of groups has a total of 7 rows representing the different groups
    The matrix of groups has a total of 3 columns, the first to identity the groups
    The first element of each row represents the group id
    the rest of the elements en in each row represent the members of that group
    When a group does not exist the group id is replaced with (empty)
    When the group has spots available, those spots are filled with (nm) representing NO MEMBER
    """
    matrix_Of_Groups =  [['add','m4','m1', 'nm'],
                        ['sub', 'm2', 'm3', 'nm'],
                        ['mul', 'm1', 'm5', 'nm'],
                        ['empty','nm','nm', 'nm'],
                        ['empty','nm','nm', 'nm'],
                        ['empty','nm','nm', 'nm'],
                        ['empty','nm','nm', 'nm']]

    mainControl(matrix_Of_Groups)

def mainControl(matrix_Of_Groups):
    option = True
    while option:
        """
        RECIEVES DATA AND SENDS CONFIRMATION
        """
        data, addr = server_socket.recvfrom(4096)



if __name__ == "__main__":
    main()
