import socket
import json


HEADER_LENGTH = 10
host = 'localhost'
port = 5432
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Group server socket created")

server_socket.bind((host, port))
print("Group server socket connected to: ", localhost)

matrix_Of_Groups =  [['add','m4','m1', 'nm', 'nm'],
                    ['sub', 'm2', 'm3', 'nm', 'nm'],
                    ['mul', 'm1', 'm4', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm'],
                    ['empty','nm','nm', 'nm', 'nm']]

matrix_Of_Clients = [['m1', 'na'],
                     ['m2', 'na'],
                     ['m3', 'na'],
                     ['m4', 'na']]

def main():
    """
    The matrix of groups has a total of 7 rows representing the different groups
    The matrix of groups has a total of 3 columns, the first to identity the groups
    The first element of each row represents the group id
    the rest of the elements en in each row represent the members of that group
    When a group does not exist the group id is replaced with (empty)
    When the group has spots available, those spots are filled with (nm) representing NO MEMBER
    """


    main_Control(matrix_Of_Groups, matrix_Of_Clients)

"""
THIS FUNCTION ADDS A CLIENT WITH ITS ADDRESS TO THE CLIENTS MATRIX
"""
def add_Client():
    for i in range(len(matrix_Of_Clients)):
        if(matrix_Of_Clients[i][0] == machine_id):
            matrix_Of_Clients[i][1] = address
            break
    return matrix_Of_Clients


"""
THIS FUNCTION WILL HANDLE THE REQUESTS FROM THE CLIENTS
AND WILL ROUTE THE REQUEST ACCORDINGLY
"""
def handle_Client(client_information):
    client = client_information[0]
    machine_ID = client_information[1]
    option = True
    while option:
        try:
            data = client.recv(4096)
            if data:
                print("Data recieved successfully")
                data = json.loads(data.decode())
                """
                MACHINE ID WILL HELP US IDENTIFY EACH SEPARATE USER
                EACH MACHINE IS ASSIGNED AN ID AS SOONAS CREATED
                M1
                M2
                M3 ETC
                """
                machine_ID = data.get("machine")
                """
                THE OPERATION VARIABLE WILL TELL ME IF THE USER WANTS TO:
                EXECUTE AN OPERATION FROM THE GROUP MANIPULATION PERSPECTIVE, IE. CREATE, DELETE, ETC
                EXECUTE A MATHEMATICA OPERATION ADD, SUB, MULY, DIVIDE
                TURN IN A RESULT FROM A REQUEST GIVEN BY THE SERVER
                """
                operation = data.get("operation")
                """
                THE INFORMATION VARIABLE WILL CONTAIN INFORMATION DEPENDING ON THE OPERATION SENT BY USER
                THE GROUP MANIPULATIONS ARE REPRESENTED FORM 1 TO 6
                THE MATHEMATICAL OPERATIONS ARE REPRESENTED FROM 1 TO 7
                THE RESULT IS REPRESENTED BY WHATEVER NUMBER THAT RESULT MAY BE
                """
                information = data.get("information")
                """
                THIS IF WILL TELL US IF THE USER WANTS TO MANIPULATE THE MATRIX OF GROUPS
                """
                if(operation == 'group'):
                    print("The user wants to manipulate the matrix of groups")
                    """
                    WE SHALL DEAL WITH THE OPTIONS IN ORDER
                    1 CREATE GROUP // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    2 DELETE GROUP // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    3 ENTER GROUP // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    4 EXIT A GROUP // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    5 SHOW THE MATRIX OF GROUPS // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    6 SEND A MESSAGE TO ALL MEMBERS OF A GROUP // MISSING BROADCAST OF RESULTING GROUPS TO USER
                    """
                    if(information == '1'):
                        matrix_Of_Groups = createGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information)
                        """
                        EDITORS NOTE: THIS FUNCTION WORKS FOR THE ADD AND SUB GROUPS
                        """
                    if(information == '2'):
                        matrix_Of_Groups = deleteGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information)
                        """
                        EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE GROUP ADD
                        """
                    if(information == '3'):
                        matrix_Of_Groups = enterGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information)
                        """
                        EDITORS NOTE: THIS FUNCTION WORKS FOR THE ADD AND SUB GROUPS
                        """
                    if(information == '4'):
                        matrix_Of_Groups = exitGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information)
                        """
                        EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE GROUP ADD
                        """
                    if(information == '5'):
                        """
                        EDITORS NOTE
                        THIS FUNCTION WILL NOT EXIST IN THE SERVER, IT WILL SEND THE MATRIX TO THE CLIENT
                        AND THE CLIENT WILL PRINT AND VIEW IT
                        """
                        broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                    if(information == '6'):
                        """
                        EDITORS NOTE WE MUST RECIEVE THE CLIENT MESSAGE AS WELL
                        """
                        broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)

                """
                THIS IF WILL TELL US IF THE USER WANTS TO PERFORM A MATH OPERATION
                """
                if(operation == 'math'):
                    print("The user wants to make a math operation")
                    """
                    WE SHALL DEAL WITH THE OPTIONS IN ORDER
                    1 add // NOT CREATED
                    2 sub // NOT CREATED
                    3 mul // NOT CREATED
                    4 div // NOT CREATED
                    5 pow // NOT CREATED
                    6 rad // NOT CREATED
                    7 log // NOT CREATED
                    THIS SECOND IF WILL CHECK WHICH MATH OPERATION THE USER WOULD LIKE TO DO
                    """
                    if(information == '1'):
                        """
                        THIS FIST WILL REPRESENT THE ADDING OPERATION
                        EDITORS NOTE: YOU MUST NOW CALL THE BROAD CAST FUNCTION
                        """
                        broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)



        except:
            client.close()
            for i in range(len(matrix_Of_Clients)):
                if(matrix_Of_Clients[i][0] == machine_ID):
                    matrix_Of_Clients[i][1] = 'na'
            for i in range(len(matrix_Of_Groups)):
                for j in range(len(matrix_Of_Groups[i])):
                    if(matrix_Of_Groups[i][j] == machine_ID):
                        matrix_Of_Groups[i][j] == 'nm'
                    break

"""
THIS FUNCTION WILL BROADCAST MESSAGES TO THE CLIENTS CORRESPONDS AND WILL RECIEVE
THE INFORMATION THAT THE CLIENTS REQUIRES AND SENDS IT TO HIM
EDITORS NOTE: THIS FUNCTION IS NOT READY
YOU ARE FIGURING OUT HOW TO HANDLE THIS FUNCTION
REMEMBER:
CLIENT - WILL ALLOWS TO COMUNICATE WITH A SPECIFIC CLIENT
OPERATION - INDICATES WETHER THE USER WANTS TO WORK WITH THE MATRIX OF GROUPS OR MATH OPERATIONS
INFORMATION - FROM THE THW POSIBLE OPTIONS OF OPERATION THERE ARE WITHIN MULTIPLE OPTIONS REPRESENTED HERE
"""
def broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information):
    print("You are about to broadcast, however we must now sort some things out")
    print("Who are we going to broadcast to")
    print("What information are we going to broadcast")
    option = True
    while option:
        """
        WE MUST VERIFY WHAT THE USER WANTS SO WE CAN GIVE IT TO HIM YEAH BABY !!
        THIS FIRST IF WILL CHECK IF THE USER WANTS TO MANIPULATE THE GROUP MATRIX
        """
        if(operation == 'group'):
            """
            THIS SECOND IF WILL TELL US THAT THE USER WISHES TO SEE THE MATRIX OF GROUPS
            SO WE HAVE TO SEND IT TO HIM
            """
            if(information == '5'):
                data_set = {"groups" : matrix_Of_Groups}
                data = json.dumps(data_set)
                client.send(data)
                confirmation_message = client.recv(4096).decode("utf-8")
            if(information == '6'):
                """
                WE MUST RECIEVE FROM THE CLIENT
                THE MESSAGE HE WANTS TO SEND
                THE GROUP HE WANTS TO SEND THE MESSAGE TO
                """
                client.send("Message&Group").encode("utf-8")
                message_And_Group = client.recv(4096).decode("utf-8")
                message_And_Group = json.loads(message_And_Group.decode("utf-8"))
                arrayData = message_And_Group.get("data")
                message = arrayData[0]
                group_ID = arraData[1]
                is_Group = alreadyGroup(matrix_Of_Groups, group_ID)
                if(is_Group == True):
                    print("The group does exist, will now send message")
                    """
                    WE NEED TO IDENTIFY ALL THE MEMBERS OF THE GROUP WE ARE
                    GOING TO SEND A MESSAGE TO
                    """
                    array_Of_Members = ['nm','nm', 'nm', 'nm']
                    if(group_ID == '1'):
                        for i in range(len(matrix_Of_Groups)):
                            if(matrix_Of_Groups[i][0] == 'add'):
                                for j in range(len(matrix_Of_Groups[i]) - 1):
                                    for k in range(len(array_Of_Members)):
                                        array_Of_Members[k] = matrix_Of_Groups[i][j+1]
                        for i in range(len(array_Members)):
                            for j in range(len(matrix_Of_Clients)):
                                if(array_Members[i] == matrix_Of_Clients[j][0]):
                                    member_address = matrix_Of_Clients[j][1]
                                    server_socket.sendto(message.encode(utf-8), member_address)
                                    confirmation_message = server_socket.recv(4096).decode("utf-8")
                                    print(confirmation_message)


        """
        THIS FIRST IF WILL CHECK IF THE USER WANTS TO DO A MATH OPERATION
        """
        if(operation == 'math'):
            """
            THIS SECOND IF WILL CHECK WHICH MATH OPERATION THE USER WOULD LIKE TO DO
            """
            if(information == '1'):
                """
                THIS FIST WILL REPRESENT THE ADDING OPERATION
                WE NEED TO CHECK IF THE ADDING GROUP EXISTS
                IF IT DOES NOT EXIST WE MUST INFORM THE USER SO THAT HE IS RETURNED TO THE MAIN MENU
                IF IT EXISTS WE MUST FIND IT'S LEADER AND ASK HIM TO CHOOSE WHO WILL DO THE MATH
                THE LEADER MUST RECIEVE THE MATRIX OF GROUPS TO DO THIS
                WHEN WE RECIEVE THE MACHINE THAT WILL DO THE MATH
                WE SEND SET MACHINE THE OPERATION AND THE MACHINE WILL RETURN THE RESULT
                WHEN THE SERVER GETS THAT RESULT IT RETURNS IT TO THE ORIGINAL CLIENT
                """






"""
THIS FUNCTION CORRESPONDS TO THE FOURTH OPTION IN THE USER CONTROLER AND WILL REMOVE A MACHINE FROM A GROUP
IF IT EXISTS
"""
def exitGroup(matrix_Of_Groups, machine_ID, information):
    print("You have chosen to exit a group")
    group_Exists = False
    is_Member = False
    option = True
    while option:
        group_ID = information
        """
        IF THE USER SELECTS 1 WE WILL DELETE THE MACHINE FROM THE ADDING GROUP
        HOWEVER WE MUST FIRS CHECK IF THE GROUP EXISTS AND IF THE MACHINE IS A MEMBER OF THE GROUP
        """
        if(group_ID == '1'):
            group_Exists = alreadyGroup(matrix_Of_Groups, group_ID)
            if(group_Exists == False):
                print("The group does not exits, therefore you cannot exit")
                print("Redirecting you to main menu")
                time.sleep(5)
                userControl(machine_Of_Groups, machine_ID)
            if(group_Exists == True):
                print("The group exists, we will now check if you are a member")
                is_Member = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
                if(is_Member == False):
                    print("You are not a member of this group, therefore you cannot exit it")
                    print("Redirecting you to the main menu")
                    time.sleep(5)
                    userControler(matrix_Of_Groups, machine_ID)
                if(is_Member == True):
                    print("You are a member of this group and will now be removed")
                    matrix_Of_Groups = removeFromGroup(matrix_Of_Groups, machine_ID, group_ID)
                    print("The new matrix of groups looks like this: ")
                    printMatrix(matrix_Of_Groups)
                    """
                    HERE WE SHOULD BROADCAST TO THE CLIENT THE NEW MATRIX OF GROUPS
                    """
                    operation = 'group'
                    information = '5'
                    broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                    time.sleep(2)
                    option = False
    return matrix_Of_Groups


def removeFromGroup(matrix_Of_Groups, machine_ID, group_ID):
    if(group_ID == '1'):
        print("\n")
        print("You are exiting the add group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j + 1] == machine_ID):
                        matrix_Of_Groups[i][j + 1] = "nm"
                        break
    return matrix_Of_Groups

"""
THIS FUNCTION CORRESPONDS TO THE THIRD OPTION IN THE USER CONTROLER AND WILL ALLOW A MACHINE
TO ENTER A GROUP IF IT EXISTS AND IF HE IS NOT ALREADY A MEMBER, IN CASE IT DOESNT EXIST IT WILL
GIVE THE USER THE POSIBILITY TO CREATE THE GROUP OR RETURN TO THE MAIN MENU
"""
def enterGroup(matrix_Of_Groups, machine_ID, information):
    print("You have chosen to enter a group")
    group_Exists = False
    is_Member = False
    option = True
    while option:
        group_ID = information
        """
        IF THE USER SELECTS 1 WE WILL INSERT THE MACHINE IN A GROUP FOR ADDING
        HOWEVER WE MUST CHECK IF THAT GROUP ALREADY EXISTS AND IF THE MACHINE IS NOT A MEMBER ALREADY
        AND DEPENDING ON THE OUTCOME WE WILL INFORM THE USER
        THE GROUP DOEST EXIST
        THE GROUP EXISTS AND YOU ARE ALREADY A MEMBER AND THEREFORE CANNOT REJOIN
        THE GROUP EXISTS AND YOU WERE NOT PREVIUSLY A MEMBER AND THEREFORE YOU WILL JOIN
        """
        if(group_ID == '1'):
            group_Exists = alreadyGroup(matrix_Of_Groups, group_ID)
            if(group_Exists == False):
                print("The group does not exist, therefore you cannot join")
                client.send("The group does not exist, therefore you cannot join").encode("utf-8")
                confirmation_message = client.recv(4096).decode("utf-8")
                time.sleep(2)
                option = False
            if(group_Exists == True):
                print("The group does exist")
                print("However in order to join you cannot already be a member")
                print("Verification in progress")
                is_Member = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
                if(is_Member == True):
                    print("You are already a member of this group and therefore cannot join")
                    client.send("You are already a member of this group and therefore cannot join").encode("utf-8")
                    confirmation_message = client.recv(4096).decode("utf-8")
                    time.sleep(2)
                    option = False
                if(is_Member == False):
                    print("You are not a member of this group and therefore may join")
                    print("Joining group")
                    matrix_Of_Groups = joinGroup(matrix_Of_Groups, machine_ID, group_ID)
                    operation = 'group'
                    information = '5'
                    broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                    time.sleep(2)
                    option = False
        if(group_ID == '2'):
            group_Exists = alreadyGroup(matrix_Of_Groups, group_ID)
            if(group_Exists == False):
                print("The group does not exist, therefore you cannot join")
                client.send("The group does not exist, therefore you cannot join").encode("utf-8")
                confirmation_message = client.recv(4096).decode("utf-8")
                time.sleep(2)
                option = False
            if(group_Exists == True):
                print("The group does exist")
                print("However in order to join you cannot already be a member")
                print("Verification in progress")
                is_Member = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
                if(is_Member == True):
                    print("You are already a member of this group and therefore cannot join")
                    client.send("You are already a member of this group and therefore cannot join").encode("utf-8")
                    confirmation_message = client.recv(4096).decode("utf-8")
                    time.sleep(2)
                    option = False
                if(is_Member == False):
                    print("You are not a member of this group and therefore may join")
                    print("Joining group")
                    matrix_Of_Groups = joinGroup(matrix_Of_Groups, machine_ID, group_ID)
                    operation = 'group'
                    information = '5'
                    broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                    time.sleep(2)
                    option = False
        print("\n")
        return matrix_Of_Groups

"""
THIS FUNCTION WILL ADD A MACHINE TO A GROUP
"""
def joinGroup(matrix_Of_Groups, machine_ID, group_ID):
    if(group_ID == '1'):
        print("\n")
        print("You are joining the add group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                for j in range(len(matrix_Of_Groups) - 1):
                    if(matrix_Of_Groups[i][j + 1] == "nm"):
                        matrix_Of_Groups[i][j + 1] = machine_ID
                        break
    if(group_ID == '2'):
        print("\n")
        print("You are joining the subtracting group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                for j in range(len(matrix_Of_Groups) - 1):
                    if(matrix_Of_Groups[i][j + 1] == "nm"):
                        matrix_Of_Groups[i][j + 1] = machine_ID
                        break
    return matrix_Of_Groups

"""
THIS FUNCTION CORRESPONDS TO THE SECOND OPTION IN THE USER CONTROLER AND IT WILL ATEMPT
TO DELETE A GROUP IF IT ALREADY EXISTS
EDITORS NOTE: IN THE PROCESS OF CREATING THE FUNCION
IN THE PROCESS OF CREATING DELETE FOR GROUP
STILL MISSING GROUPS 2 TO 7
"""
def deleteGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information):
    print("You have chosen to delete a group")
    is_Already_Group = False
    option = True
    while option:
        group_ID = information
        """
        IF THE USER SELECTS 1 WE WILL DELETE A GROUP FOR ADDING
        HOWEVER WE MUST CHECK IF THAT GROUP ALREADY EXISTS, AND IF SO
        WE WILL DELETE IT, IF NOT WE LET THE USER KNOW IT DID NOT EXIST
        """
        if(group_ID == '1'):
            print("You have chosen to delete the adding group: ")
            print("However we must now check if the group exists")
            is_Already_Group = alreadyGroup(matrix_Of_Groups, group_ID)
            if(is_Already_Group == False):
                print("The group does not exist and therefore cannot be deleted")
                print("Informing user")
                client.send("The group does not exist and therefore cannot be deleted").encode("utf-8")
                confirmation_message = client.recv(4096).decode("utf-8")
                print(confirmation_message)
                time.sleep(2)
                option = False
            if(is_Already_Group == True):
                print("The adding group exists, and will now be deleted")
                matrix_Of_Groups = removeGroup(matrix_Of_Groups, group_ID)
                print("The new matrix of groups looks like this: ")
                printMatrix(matrix_Of_Groups)
                """
                HERE WE SHOULD BROADCAST TO THE CLIENT THE NEW MATRIX OF GROUPS
                """
                operation = 'group'
                information = '5'
                broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                time.sleep(2)
                option = False
        print("\n")
        return matrix_Of_Groups

"""
THIS FUNCTION DELETES A GROUP BY REMOVING ALL OF ITS INFORMATION
FOR THE GROUP ID WILL BE REPLACED WITH (empty)
FOR THE GROUP MEMBERS WILL BE REPLACED WITH (nm) NO MEMBER
"""
def removeGroup(matrix_Of_Groups, group_ID):
    if(group_ID == '1'):
        print("You are deleting the add group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                matrix_Of_Groups[i][0] = "empty"
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    matrix_Of_Groups[i][j + 1] = "nm"
    return matrix_Of_Groups

"""
THIS FUNCTION CORRESPONDS TO THE FIRST OPTION IN THE USER CONTROLER AND IT WILL ATEMPT
TO CREATE A GROUP IF IT DOESN'T ALREADY EXISTS
EDITORS NOTE: THIS FUNCTION IS IN PROGRESS
ITS STILL MISSING ALL THE GROUPS FROM 2 TO 7
HOWEVER THE CODE FORM GROUP 1 IS REUSABLE, SO ITS A MATTER OF TESTING EVERYTHING FIRST BEFORE GENERALIZING
"""
def createGroup(matrix_Of_Groups,matrix_Of_Clients, machine_ID, client, operation, information):
    print("You have chosen to create a group")
    is_Already_Group = False
    option = True
    while option:
        group_ID = information
        """
        IF THE USER SELECTS 1 WE WILL CREATE A GROUP FOR ADDING
        HOWEVER WE MUST CHECK IF THAT GROUP ALREADY EXISTS, AND IF SO
        WE WILL ASK THE USER IF HE WOULD LIKE TO JOIN
        """
        if(group_ID == '1'):
            print("You have chosen to create an adding group")
            print("However we must now check if the group exists already")
            is_Already_Group = alreadyGroup(matrix_Of_Groups, group_ID)
            if(is_Already_Group == True):
                print("The group add already exists")
                client.send("The group add already exists").encode("utf-8")
                confirmation_message = client.recv(4096).decode("utf-8")
                print(confirmation_message)
                time.sleep(2)
                option = False
            if(is_Already_Group == False):
                print("The group does not exist, creating now, you will be the leader")
                matrix_Of_Groups = addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID)
                print("The new matrix of groups looks like this: ")
                printMatrix(matrix_Of_Groups)
                """
                HERE WE SHOULD BROADCAST TO THE CLIENT THE NEW MATRIX OF GROUPS
                """
                operation = 'group'
                information = '5'
                broadcast(matrix_Of_Groups, matrix_Of_Clients, client, operation, information)
                time.sleep(2)
                option = False
    return matrix_Of_Groups

"""
THIS FUNCTION WILL CREATE A GROUP AND INSERT THE PERSON WHO CREATED IT TO THE GROUP
EDITORS NOTE: THIS FUNCTION IS READY
"""
def addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID):
    if(group_ID == '1'):
        print("\n")
        print("You are creating the add group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'empty'):
                matrix_Of_Groups[i][0] = "add"
                matrix_Of_Groups[i][1] = machine_ID
                break
    return matrix_Of_Groups


"""
THIS FUNCTION WILL CHECK IF A GROUP ALREADY EXISTS
EDITORS NOTE: THIS FUNCTION IS STILL A WORK IN PROGRESS
IS MISSING GROUPS 3 TO 7
"""
def alreadyGroup(matrix_Of_Groups, group_ID):
    is_Already_Group = False
    if(group_ID == '1'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                is_Already_Group = True
                break
    if(group_ID == '2'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                is_Already_Group = True
                break
    return is_Already_Group

"""
THIS FUNCTION WILL CHECK IF A COMPUTER IS ALREADY MEMBER OF A GROUP
EDITORS NOTE: THIS FUNCTION IS STILL A WORK IN PROGRESS
IS MISSING GROUPS 3 TO 7
"""
def alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID):
    is_Member = False
    if(group_ID == '1'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        is_Member = True
                        break
    if(group_ID == '2'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        is_Member = True
                        break
    return is_Member


"""
THIS FUNCTION IS RESPONSABLE FOR HANDDLING INCOMING MESSAGES AND
IT WILL EITHER HANDDLE A NEW CLIENT OR A PRE-EXISTING ONE
"""
def main_Control(matrix_Of_Groups, matrix_Of_Clients):
    option = True
    while option:
        print("Group Server is running and listening...")
        client, address = server.accept()
        print("Connection is established with ", {str(address)})
        client.send("MachineID".encode("utf-8"))
        machine_ID = client.recv(4096).decode("utf-8")
        matrix_Of_Clients = add_Client(machine_ID, address)
        client_information = [client, machine_ID]
        handle_Client(client_information)


if __name__ == "__main__":
    main()
