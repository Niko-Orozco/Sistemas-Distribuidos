import socket
import json
import time
"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANDREI OROZCO
"""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client socket created")

host = 'localhost'
port = 5433

machine_id = 'm1'
server_addr = 0

"""
THIS FUNCTION REPRESENTS THE MENU FROM WHICH
THE USER CAN SELECT ALL THE OPTIONS
REGARDING THE GROUPS
EDITORS NOTE: NOT READY ALL MISSING
"""
def math_Menu(machine_id):
    """
    OPERATION WILL LET THE SERVER KNOW
    WHEN THE USER HAS SELECTED TO MANIPULATE THE GROUPS
    OR AT LEAST WORK WITH THIS OPTION
    """
    operation = '1'
    """
    INFORMATION WILL LET THE SERVER KNOW
    FROM THIS MENU OF OPTION WHAT THE USER WANTS TO DO
    """
    information = '0'
    data_Array= []



"""
THIS FUNCTION WILL SHOW THE
USER THE GROUPS WITH ALL THEIR RESPECTIVE MEMBERS
EDITORS NOTE: THIS FUNCTION IS READY
"""
def printMatrix(matrix_of_groups):
    for i in range(len(matrix_of_groups)):
        if(matrix_of_groups[i][0] != 'empty'):
            print("Group: ", matrix_of_groups[i][0])
            for j in range(len(matrix_of_groups[i]) - 1):
                if(matrix_of_groups[i][j+1] != 'nm'):
                    print("Members: ", matrix_of_groups[i][j+1])

"""
THIS FUNCTION REPRESENTS THE MENU FROM WHICH
THE USER CAN SELECT ALL THE OPTIONS
REGARDING THE GROUPS
EDITORS NOTE: NOT READY ALL MISSING
NOT TESTED
"""
def group_Menu(machine_id):
    """
    OPERATION WILL LET THE SERVER KNOW
    WHEN THE USER HAS SELECTED TO MANIPULATE THE GROUPS
    OR AT LEAST WORK WITH THIS OPTION
    """
    operation = '1'
    """
    INFORMATION WILL LET THE SERVER KNOW
    FROM THIS MENU OF OPTION WHAT THE USER WANTS TO DO
    """
    information = '0'
    option = True
    while option:
        print("Welcome to this service")
        print("Press 1 to create a group")
        print("Press 2 to delete a group")
        print("Press 3 to enter a group")
        print("Press 4 to exit a group")
        print("Press 5 to show the matrix of groups")
        print("Press 6 to send a message to a group")
        opt = input("Please enter your selection:")
        print("\n")

        """
        THIS PART WILL CONTROL WHAT HAPPENS BASED ON YOUR SELECTION
        """
        if(opt == '1'):
            print("You have chosen to creat a group")
            print("Which group would you like to create: ")
            print("Press 1 for add")
            print("Press 2 for subtract")
            print("Press 3 for multiply")
            print("Press 4 for divide")
            print("Press 5 for power")
            print("Press 6 for radical")
            print("Press 7 for logarithm")
            op = input("Please enter your selection:")
            print("\n")
            if(op == '1'):
                information = '1'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The add group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)
            if(op == '2'):
                information = '2'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The sub group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)
            if(op == '3'):
                information = '3'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The mul group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)
            if(op == '4'):
                information = '4'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The div group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)

            if(op == '5'):
                information = '5'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The pow group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)

            if(op == '6'):
                information = '6'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The rad group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)

            if(op == '7'):
                information = '7'
                data_array = [machine_id, operation, information]
                data_set = {'data': data_array}
                data = json.dumps(data_set)
                client_socket.sendto(data.encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                print(confirmation_message)

                client_socket.sendto("Proceed".encode(), (host, 5432))

                confirmation_message, server_addr = client_socket.recvfrom(4096)
                confirmation_message = confirmation_message.decode()
                if(confirmation_message == 'AE'):
                    print("The log group already exists")
                    time.sleep(2)
                    client_Main_Menu(machine_id)

                if(confirmation_message == 'DE'):
                    print("The group does not exist and will now be created")
                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    data, server_addr = client_socket.recvfrom(4096)
                    if data:
                        print("Data recieved with matrix")
                        data = json.loads(data.decode())
                        matrix_of_groups = data.get("groups")
                        printMatrix(matrix_of_groups)


                    client_socket.sendto("Proceed".encode(), (host, 5432))

                    time.sleep(2)
                    client_Main_Menu(machine_id)
"""
IN THIS FUNCTION THE CLIENT WILL SELECT THEIR DESIRED
CURSE OF ACTION AS DISCUSED IN THE COMMENTS IN MAIN
"""
def client_Main_Menu(machine_id):
    option = True
    while option:
        print("To visualize the group manipulation menu press 1")
        print("To visualize the math operations menu press 2")
        opt = input("Please enter your selection: ")
        if(opt == '1'):
            group_Menu(machine_id)
        if(opt == '2'):
            math_Menu(machine_id)

"""
THIS FUNCTION WILL ESTABLISH FIRST CONTACT BETWEEN A CLIENT
AND THE SERVER
"""
def client_Comunication():
    print("Will now attemp comunication with server")
    """
    SENDING SERVER OUT MACHINE ID SO THAT WE CAN BE IDENTIFIED
    """
    client_socket.sendto(machine_id.encode(), (host, 5432))

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
    client_Main_Menu(machine_id)

def main():
    client_Comunication()

if __name__ == "__main__":
    main()
