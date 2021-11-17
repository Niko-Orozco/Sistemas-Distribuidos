import socket
import json


"""
CODE BY:
JACOBO OROZCO ARDILA
NICOLAS ANREI OROZCO
"""
client_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client Socket Created')
host = '127.0.0.1'
port = 5433
client_socket.connect((host, 5432))

"""
WHAT DOES THE USER NEED?
CREATE, DELETE, ENTER OR EXIT ANY GROUP. ANY USER MAY BE PART OF ANY GROUP
LIST THE EXISTING GROUPS
SEND A MESSAGE TO ANY GROUP
"""
machine_ID = 'm1'

def main():
    clientRecieve(machine_ID)




def clientRecieve(machine_ID):
    option = True
    while option:
        try:
            message = client_socket.recv(4096).decode("utf-8")
            if(message == 'MachineID'):
                client_socket.send(machine_ID.encode("utf-8"))
            else:
                print(message)
            if(message == 'Request'):
                clientSend(machine_ID)
        except Exception as e:
            print(e)
            client_socket.close()
            break

"""
THIS FUNCTION MANAGES THE DIFERENT MENUS AND THE SENDING OF MESSAGES TO SERVER
FOR GROUPS:
THE SERVER EXPECTS: JSON WITH = MACHINEID, OPERATION, INFORMATION
"""
def clientSend(machine_ID):
    option = True
    while option:
    """
    AQUI SE UBICA TODA MI LOGICA PARA EL ENVIO DE MENSAJES
    AQUI ELEGIRE EL MENU DESDE EL CUAL DESEO ENVIAR LAS COSAS
    PARA MANIPULACION DE GRUPOS
    PARA OPERACIONES MATEMATICAS
    """
    print("To manipulate the matrix of groups press 1")
    print("To do a math operation press 2")
    opt = input("Please enter your selection: ")
    if(opt = '1'):
        data_Array = groupController(machine_ID)
        machine_ID = data_Array[0]
        operation = data_Array[1]
        information = data_Array[2]
        data_Set = {"machine": machine_ID, "operation" : operation, "information": information}
        data = json.dumps(data_Set)
        client_socket.send(data.encode("utf-8"))

    if(opt = '2'):
        mathController(machine_ID)


def groupController(machine_ID):
    operation = '1'
    information = '0'
    data_Array = []
    option = True
    while option:
        print("Welcome to this service")
        print("Press 1 to create a group")
        print("Press 2 to delete a group")
        print("Press 3 to enter a group")
        print("Press 4 to exit a group")
        print("Press 5 to show the matrix of groups")
        print("Press 6 to send a message to a group")
        print("Press 7 to compact on a JSON")
        opt = input("Please enter your selection:")
        print("\n")
        """
        THIS PART CONTROLS WHAT HAPPENS DEPENDING ON WHAT THE USER SELECTED
        """
        if opt == '1':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE: THIS COMMS ARE NOT WORKING
            """
        if opt == '2':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE: THIS COMMS ARE NOT WORKING
            """
        if opt == '3':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE:  THIS COMMS ARE NOT WORKING
            """
        if opt == '4':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE:  THIS COMMS ARE NOT WORKING

            """
        if opt == '5':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE:  THIS COMMS ARE NOT WORKING
            """
        if opt == '6':
            information = opt
            data_Array = [machine_ID, operation, information]
            option = False
            """
            EDITORS NOTE:  THIS COMMS ARE NOT WORKING, DOES NOT EXIST
            THIS IS THE NEXT STEP
            """
        print("\n")
    return data_Array






if __name__ == "__main__":
    main()
