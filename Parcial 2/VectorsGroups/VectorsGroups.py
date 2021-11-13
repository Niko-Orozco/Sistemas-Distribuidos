import numpy as np
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
    from the second onward to identify the members of set group
    """
    matrix_Of_Groups = np.array([['empty','nm','nm'],
                                 ['sub', 'm2', 'm3'],
                                 ['mul', 'm1', 'm5'],
                                 ['empty','nm','nm'],
                                 ['empty','nm','nm'],
                                 ['empty','nm','nm'],
                                 ['empty','nm','nm']])
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
            EDITORS NOTE: THIS FUNCTION WORKS ONLY FOR THE SUM GROUP
            """
        if opt == '2':
            matrix_Of_Groups = deleteGroup(matrix_Of_Groups)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT READY
            """
        if opt == '3':
            matrix_Of_Groups = enterGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
            """
        if opt == '4':
            matrix_Of_Groups = exitGroup(matrix_Of_Groups, machine_ID)
            """
            EDITORS NOTE: THIS FUNCTION IS NOT CREATED, DOES NOT EXIST
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
            """

"""
THIS FUNCTION CORRESPONDS TO THE FIFTH OPTION IN THE USER CONTROLER AND WILL SHOW THE
USER THE GROUPS WITH ALL THEIR RESPECTIVE MEMBERS
"""
def printMatrix(matrix_Of_Groups):
    for i in range(len(matrix_Of_Groups)):
        if(matrix_Of_Groups[i][0] != 'empty'):
            print("Group: ", matrix_Of_Groups[i][0])
            for j in range(len(matrix_Of_Groups[i]) - 1):
                if(matrix_Of_Groups[i][j+1] != 'nm'):
                    print("Members: ", matrix_Of_Groups[i][j+1])

"""
THIS FUNCTION CORRESPONDS TO THE SECOND OPTION IN THE USER CONTROLER AND IT WILL ATEMPT
TO DELETE A GROUP IF IT ALREADY EXISTS
"""
def deleteGroup(matrix_Of_Groups):
    print("You have chosen to create a group")
    is_Already_Group = False
    option = False
    while option:
        printMenu()
        group_ID = input("Which group would you like to delete: ")
        """
        IF THE USER SELECTS 1 WE WILL DELETE A GROUP FOR ADDING
        HOWEVER WE MUST CHECK IF THAT GROUP ALREADY EXISTS, AND IF SO
        WE WILL DELETE IT, IF NOT WE LET THE USER KNOW IT DID NOT EXIST
        """
        if(group_ID == '1'):
            print("You have chosen to delete an adding group: ")
            print("However we must now check if the group exists already")
            is_Already_Group = alreadyGroup(matrix_Of_Groups, group_ID)
            if(is_Already_Group == False):
                print("The group does not exist and therefore cannot be deleted")
                print("Redirecting you to main menu")
"""
THIS FUNCTION CORRESPONDS TO THE FIRST OPTION IN THE USER CONTROLER AND IT WILL ATEMPT
TO CREATE A GROUP IF IT DOESN'T ALREADY EXISTS
EDITORS NOTE: THIS FUNCTION IS IN PROGRESS
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
"""
def addGroupToMatrix(matrix_Of_Groups, machine_ID, group_ID):
    if(group_ID == '1'):
        print("You are creating the sum group")
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'empty'):
                matrix_Of_Groups[i][0] = "sum"
                matrix_Of_Groups[i][1] = machine_ID
                break
    return matrix_Of_Groups

"""
THIS FUNCTION WILL CHECK IF A GROUP ALREADY EXISTS
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
"""
def alreadyInGroup(matrix_Of_Groups, machine_ID, group_ID):
    is_Already_In_Group = False
    if(group_ID == '1'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'add'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        is_Already_In_Group = True
                        break
    if(group_ID == '2'):
        for i in range(len(matrix_Of_Groups)):
            if(matrix_Of_Groups[i][0] == 'sub'):
                for j in range(len(matrix_Of_Groups[i]) - 1):
                    if(matrix_Of_Groups[i][j+1] == machine_ID):
                        is_Already_In_Group = True
                        break
    return is_Already_In_Group

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


if __name__ == "__main__":
    main()
