import numpy as np
import time

"""
    matrix_Of_Groups = np.array([ ['suma', -10, 15],
                    ['resta', -6, 9],
                    ['multiplicacion', 8, 12],
                    ['division', 8, 12],
                    ['potenciacion', 8, 12],
                    ['radicacion', 8, 12],
                    ['logaritmacion', 8, 12]])
STILL HAVE TO FIGURE OUT HOW TO CREATE AN EMPTY MATRIX AND THEN FILL IT
"""

def main():
    """
    THIS WILL BE THE EMPTY MATRIX OF GROUPS

    THE MATRIX OF GROUPS WILL HAVE 7 ROWS (CORRESPONDING TO THE 7 POSIBLE GROUPS)
    THE MATRIX OF GROUPS WILL HAVE
        matrix_Of_Groups = np.array([
                                     ['sub', 'm2', 'm3'],
                                     ['mul', 'm1', 'm5']])
    """
    matrix_Of_Groups = np.empty((6, 6))

    """
    EDITORS NOTE:
    THIS WILL IDENTIFY THE CLIENT AND WILL BE PASSED TO THE GROUP SERVER
    """
    machine_ID = "m1";
    userControler(matrix_Of_Groups, machine_ID)

"""
THE USERCONTROLER GIVES THE USER THE ABILITY TO WORK WITH THE GROUP MATRIX
IN ORDER TO
CREATE A GROUP
DELETE A GROUP
ENTER A GROUP
EXIT A GROUP
LIST THE EXISTING GROUPS
AND SEND A MESSAGE TO ALL MEMBERS OF A GROUP
"""
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
        opt = input("Please enter your selection:")
        """
        THIS PART CONTROLS WHAT HAPPENS DEPENDING ON WHAT THE USER SELECTED
        """

        """
        IF THE OPTION IN EQUAL TO 1 THEN THE USER DESIRES TO CREATE A GROUP
        """
        if opt == '1':
            matrix_Of_Groups = createGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: YOU ARE ABOUT TO CREATE THE CREATE GROUP FUNCTION
            """
        if opt == '2':
            deleteGroup(matrix_Of_Groups)
            """
            EDITORS NOTE: THIS FUNCTION IS READY
            """
        if opt == '3':
            enterGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
            """
        if opt == '4':
            exitGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
            """
        if opt == '5':
            showMatrix(matrix_Of_Groups)
            """
            EDITORS NOTE: THIS FUNCTION IS READY
            """
        if opt == '6':
            sendMessageGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
            """
"""
THE CREATE GROUP FUNCTIONS ENABLES A USER TO CREATE ANY OF THE GROUPS
ADDING -- ADD
SUBTRACTING -- SUB
MULTIPLYING -- MUL
DIVIDING -- DIV
POTENTIATION -- POW
RADICATION -- RAD
LOGARITHM -- LOG

EDITORS NOTE: THIS FUNCTION IS A WORK IS PROGRESS
"""
def createGroup(matrix_Of_Groups, machine_ID):
    print("You have choosen to create a group")
    option = True
    while option:
        printMenu()
        group_ID = input("Which group would you like to create? ")
        """
        IF THE USER SELECTS 1 WE WILL CREATE A GROUP FOR ADDING
        HOWEVER WE MUST CHECK IF THAT GROUP ALREADY EXISTS, AND IF SO
        WE WILL ASK THE USER IF HE WOULD LIKE TO JOIN
        """
        if(group_ID == '1'):
            matrix_Of_Groups = addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID)
            option = False
            print("The new matrix of groups after creating the addition group")
            showMatrix(matrix_Of_Groups)
            time.sleep(5)
    return matrix_Of_Groups

"""
EDITORS NOTE: YOU ARE IN PROGRESS OF CREATING THE CREATESGROUP FUNCTION
"""
def addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID):
    group_Exists = False
    if(group_ID == '1'):
        print("You have chosen to create a sum group")
        print("However we must first identify if the group exists")
        group_Exists = alreadyGroup(matrix_Of_Groups, group_ID)
        if(group_Exists == True):
            print("The group for adding already exists")
            print("To join the group press 0")
            print("To return to main manu press 1")
            print("To return to creation menu press 2")
            join_Group = input("Please enter your selection: ")
            if(join_Group == '0'):
                """
                EDITORS NOTE: THIS FUNCTION DOES NOT EXIST
                """
                matrix_Of_Groups = joinGroup(matrix_Of_Groups, machine_ID, group_ID)
            if(join_Group == '1'):
                userControler(matrix_Of_Groups, machine_ID)
            if(join_Group == '2'):
                createGroup(matrix_Of_Groups, machine_ID)
        if(group_Exists == False):
            print("The adding group does not exist, therefore we shall create one")
            print("Since the group didn't exist, you shall be the leader")
            new_Group = np.array(['add', machine_ID, 'm3'])
            print("The new matrix for addint to the matrix of groups")
            showMatrix(new_Group)
            matrix_of_Groups = np.append(matrix_Of_Groups, [new_Group], axis = 0)
            print("The new matrix of groups after creating the addition group")
            showMatrix(matrix_Of_Groups)

    return matrix_Of_Groups

"""
THIS FUNCTION IS USED TO INSERT A CLIENT IN A GROUP, IF HE IS NOT ON IT ALREADY
"""
def joinGroup(matrix_Of_Groups, machine_ID, group_ID):
    print("You have chosen to join the group: ",group_ID)
    print("However we must be sure you aren't already in the group")
    already_In_Group = alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID)
    if(already_In_Group == True):
        print("You are already a part of the group")
        print("To return to main manu press 0")
        print("To return to creation menu press 1")
        to_Menu = input("Please enter your selection: ")
        if(to_Menu == 0):
            userControler(matrix_Of_Groups, machine_ID)
        if(to_Menu == 1):
            createGroup(matrix_Of_Groups, machine_ID)
    if(already_In_Group == False):
        if(group_ID == '1'):
            for i in range(len(matrix_Of_Groups)):
                if(matrix_Of_Groups[i][0] == 'add'):
                    matrix_Of_Groups[i] = np.append(matrix_Of_Groups[i][1], machine_ID)
                    break
    return matrix_Of_Groups

"""
THIS FUNCTION DETERMINES WETHER A CLIENT IS MEMBER OF A GROUP GROUP OR NOT
IF THE MEMBER EXISTS IT RETURNS TRUE
IF THE MEMBER DOES NOT EXISTS IT RETURNS FALSE
"""
def alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID):
    already_In_Group = False
    if(group_ID == '1'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '2'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '3'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'mul'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '4'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'div'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '5'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'pow'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '6'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'rad'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break
    if(group_ID == '7'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'log'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        alreadyInGroup = True
                        break

    return alreadyInGroup
"""
THIS FUNCTION DETERMINES WETHER A GROUP EXISTS OR NOT
IF THE GROUP EXISTS IT RETURNS TRUE
IF THE GROUP DOES NOT EXISTS IT RETURNS FALSE
"""
def alreadyGroup(matrix_Of_Groups, group_ID):
    group_Exists = False
    if(group_ID == '1'):
        for i in range(len(matrix_Of_Groups)):
            if(np.any(matrix_Of_Groups == 'add')):
                group_Exists = True
                break
    if(group_ID == '2'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                group_Exists = True
                break
    if(group_ID == '3'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'mul'):
                group_Exists = True
                break
    if(group_ID == '4'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'div'):
                group_Exists = True
                break
    if(group_ID == '5'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'pow'):
                group_Exists = True
                break
    if(group_ID == '6'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'rad'):
                group_Exists = True
                break
    if(group_ID == '7'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'log'):
                group_Exists = True
                break
    return group_Exists
"""
THE DELETEGROUP FUNCTIONS LOOKS FOR A PREDETIRMED TAG PLACED WITHIN THE MATRIX OF GROUPS
WHICH INDICATE THE GROUP, WHEN AND IF IT FINDS THE DESIRED GROUP TO DELETE
"""
def deleteGroup(matrix_Of_Groups):
    printMenu()
    group_Name = input("Which group would you like to delete?: ")
    group_Deleted = False
    if(group_Name == '1'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Name == '2'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Name == '3'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'mul'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break

    if(group_Name == '4'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'div'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Name == '5'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'pow'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Name == '6'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'rad'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Name == '7'):
        location_Of_Group = 0
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'log'):
                matrix_Of_Groups = np.delete(matrix_Of_Groups, (i), axis = 0)
                group_Deleted = True
                break
    if(group_Deleted == True):
        print("Group Deleted Successfully")
    if(group_Deleted == False):
        print("Group could not be deleted because it did not exist")
    time.sleep(5)
    return matrix_Of_Groups

"""
THIS FUNCTION WILL PROVIDE A REUSABLE HANDY MENU
"""
def printMenu():
    print("Press 1 for add")
    print("Press 2 for subtract")
    print("Press 3 for multiply")
    print("Press 4 for divide")
    print("Press 5 for power")
    print("Press 6 for radical")
    print("Press 7 for logarithm")

"""
THIS FUNCTION WILL SHOW THE ENTIRE MATRIX IN ITS PURE FORM
"""
def showMatrix(matrix_Of_Groups):
    print("Matrix of groups: ")
    print(matrix_Of_Groups)

"""
THIS FUNCTION WILL LIST ALL THE SEPARATE GROUPS WITH ITS MEMBERS
"""
def showGroups(matrix_Of_Groups):
    for i in range(len(matrix_Of_Groups)):
        print("Members of group: ",matrix_Of_Groups[i][0])
        array1 = matrix_Of_Groups[i]
        for j in range(1, len(array1)):
            print(array1[j])
    print("Those are all the groups")

if __name__ == "__main__":
    main()
