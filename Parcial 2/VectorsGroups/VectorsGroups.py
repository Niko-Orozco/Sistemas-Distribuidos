import time
import json
"""
AUTHORS:
JACOBO OROZCO ARDILA
NICOLAS ANDREI OROZCO
"""

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
    """
    This id will help identify the computer
    """
    machine_ID = "m1"
    userControler(matrix_Of_Groups, machine_ID)


def userControler(matrix_Of_Groups, machine_ID):
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
            matrix_Of_Groups = createGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE ADD GROUP
            """

        if opt == '2':
            matrix_Of_Groups = deleteGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE GROUP ADD
            """
        if opt == '3':
            matrix_Of_Groups = enterGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION WORKS FOR THE ADD AND SUB GROUPS
            """
        if opt == '4':
            matrix_Of_Groups = exitGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE GROUP ADD

            """
        if opt == '5':
            printMatrix(matrix_Of_Groups)
            """
            EDITORS NOTE: THIS FUNCTION IS READY
            """
        if opt == '6':
            sendMessageGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
            THIS IS THE NEXT STEP
            """
        if opt == '7':
            matrix_Of_Groups = compactJson(matrix_Of_Groups, machine_ID)
        print("\n")

def compactJson(matrix_Of_Groups, machine_ID):
    data_Set = {"groups": matrix_Of_Groups, "machine": machine_ID}
    data = json.dumps(data_Set)
    print(data)
    matrix_Of_Groups = showJson(data)
    return matrix_Of_Groups

def showJson(data):
    json_Object = json.loads(data)
    matrix_Of_Groups = json_Object["groups"]
    return matrix_Of_Groups
"""
THIS FUNCTION CORRESPONDS TO THE FIFTH OPTION IN THE USER CONTROLER AND WILL SHOW THE
USER THE GROUPS WITH ALL THEIR RESPECTIVE MEMBERS
EDITORS NOTE: THIS FUNCTION IS READY
"""
def printMatrix(matrix_Of_Groups):
    for i in range(len(matrix_Of_Groups)):
        if(matrix_Of_Groups[i][0] != 'empty'):
            print("Group: ", matrix_Of_Groups[i][0])
            for j in range(len(matrix_Of_Groups[i]) - 1):
                if(matrix_Of_Groups[i][j+1] != 'nm'):
                    print("Members: ", matrix_Of_Groups[i][j+1])

"""
THIS FUNCTION CORRESPONDS TO THE FOURTH OPTION IN THE USER CONTROLER AND WILL REMOVE A MACHINE FROM A GROUP
IF IT EXISTS
"""
def exitGroup(matrix_Of_Groups, machine_ID):
    print("You have chosen to exit a group")
    group_Exists = False
    is_Member = False
    option = True
    while option:
        printMenu()
        group_ID = input("Which group would you like to exit: ")
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
                    time.sleep(5)
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
def enterGroup(matrix_Of_Groups, machine_ID):
    print("You have chosen to enter a group")
    group_Exists = False
    is_Member = False
    option = True
    while option:
        printMenu()
        group_ID = input("Which group would you like to join: ")
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
                print("Would you like to create the adding group")
                print("Press 1 for yes")
                print("Press 0 for no")
                opt = input("Please enter your selection: ")
                if(opt == '0'):
                    print("You have elected not to create the group")
                    print("Redirecting you to main menu")
                    time.sleep(5)
                    userControl(machine_Of_Groups, machine_ID)
                if(opt == '1'):
                    print("You have elected to create the group")
                    print("Redirecting you the creating menu")
                    print("\n")
                    matrix_Of_Groups = createGroup(matrix_Of_Groups, machine_ID)
                    option = False
            if(group_Exists == True):
                print("The group does exist")
                print("However in order to join you cannot already be a member")
                print("Verification in progress")
                is_Member = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
                if(is_Member == True):
                    print("You are already a member of this group and therefore cannot join")
                    print("Redirecting you to main menu")
                    time.sleep(5)
                    userControler(matrix_Of_Groups, machine_ID)
                if(is_Member == False):
                    print("You are not a member of this group and therefore may join")
                    print("Joining group")
                    matrix_Of_Groups = joinGroup(matrix_Of_Groups, machine_ID, group_ID)
                    print("The new matrix of groups looks like this: ")
                    printMatrix(matrix_Of_Groups)
                    time.sleep(5)
                    option = False
        if(group_ID == '2'):
            group_Exists = alreadyGroup(matrix_Of_Groups, group_ID)
            if(group_Exists == False):
                print("The group does not exist, therefore you cannot join")
                print("Would you like to create the subtracting group")
                print("Press 1 for yes")
                print("Press 0 for no")
                opt = input("Please enter your selection: ")
                if(opt == '0'):
                    print("You have elected not to create the group")
                    print("Redirecting you to main menu")
                    time.sleep(5)
                    userControl(machine_Of_Groups, machine_ID)
                if(opt == '1'):
                    print("You have elected to create the group")
                    print("Redirecting you the creating menu")
                    print("\n")
                    matrix_Of_Groups = createGroup(matrix_Of_Groups, machine_ID)
                    option = False
            if(group_Exists == True):
                print("The group does exist")
                print("However in order to join you cannot already be a member")
                print("Verification in progress")
                is_Member = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
                if(is_Member == True):
                    print("You are already a member of this group and therefore cannot join")
                    print("Redirecting you to main menu")
                    time.sleep(5)
                    userControler(matrix_Of_Groups, machine_ID)
                if(is_Member == False):
                    print("You are not a member of this group and therefore may join")
                    print("Joining group")
                    matrix_Of_Groups = joinGroup(matrix_Of_Groups, machine_ID, group_ID)
                    print("The new matrix of groups looks like this: ")
                    printMatrix(matrix_Of_Groups)
                    time.sleep(5)
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
def deleteGroup(matrix_Of_Groups, machine_ID):
    print("You have chosen to delete a group")
    is_Already_Group = False
    option = True
    while option:
        printMenu()
        group_ID = input("Which group would you like to delete: ")
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
                print("Redirecting you to main menu")
                time.sleep(5)
                userControler(matrix_Of_Groups, machine_ID)
            if(is_Already_Group == True):
                print("The adding group exists, and will now be deleted")
                matrix_Of_Groups = removeGroup(matrix_Of_Groups, group_ID)
                print("The new matrix of groups looks like this: ")
                printMatrix(matrix_Of_Groups)
                time.sleep(5)
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
def createGroup(matrix_Of_Groups, machine_ID):
    print("You have chosen to create a group")
    is_Already_Group = False
    option = True
    while option:
        printMenu()
        group_ID = input("Which group would you like to create: ")
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
                time.sleep(5)
                userControler(matrix_Of_Groups, machine_ID)
            if(is_Already_Group == False):
                print("The group does not exist, creating now, you will be the leader")
                matrix_Of_Groups = addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID)
                print("The new matrix of groups looks like this: ")
                printMatrix(matrix_Of_Groups)
                time.sleep(5)
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
THIS FUNCTION WILL PROVIDE A REUSABLE HANDY MENU
EDITORS NOTE: THIS FUNCTION IS READY
"""
def printMenu():
    print("Press 1 for add")
    print("Press 2 for subtract")
    print("Press 3 for multiply")
    print("Press 4 for divide")
    print("Press 5 for power")
    print("Press 6 for radical")
    print("Press 7 for logarithm")
    print("\n")


if __name__ == "__main__":
    main()
