import TISTAPY as TP
IGNOREVALUE = -999


def errorDetection(errorNumber):
    print("\n")
    print("ERROR!!! ")

    if errorNumber == 1:
        print("[1]#! - You have entered an invalid or non-existent option.")

    elif errorNumber == 2:
        print("[2]#! - You are required to enter integer values ​​to navigate the menus.")

    else:
        pass

    print("Please try again.")
    return errorNumber

def wantGoToMenu():

    while True:
        print("Go to main manu? ")
        print("[1] - Yes \n[2] - No")

        try:
            goToMenu = int(input(">>> "))
        except:
            errorDetection(2)
            goToMenu = IGNOREVALUE
    

        if goToMenu == 1:
            return True
        elif goToMenu == 2:
            return False
        elif goToMenu == IGNOREVALUE:
            pass
        else:
            errorDetection(1)

def infoTP():
    while True:
        print("TISTAPY is a python module specifically for TI calculators.")

        if wantGoToMenu():
            break


def z_testMenu():
    pass


def main ():
    print("\nWelcome to TISTAPY - Statistics on TI-84 CE with Python")


    while True:

        print("Select an option: ")
        print("[1] - Info")
        print("[2] - Z-Test")
        print("[3] - ")
        print("[4] - ")
        print("[5] - ")
        print("[6] - ")
        print("[0] - Exit the program")

        try:
            menuOption = int(input(">>> "))
        except:
            errorDetection(2)
            menuOption = IGNOREVALUE
        
        if menuOption == 0:
            break

        elif menuOption == 1:
            print("\n>>>Info<<<")
            infoTP()

        elif menuOption == 2:
            print("\n>>>Z-Test<<<")

        elif menuOption == IGNOREVALUE:
            pass

        else:
            errorDetection(1)



if __name__ == "__main__":
    main()