from ti_system import disp_clr as dc
import time


def print32 (prompt: str = "", lineLength: int = 32) -> str:
    """
    This print is a special print for TI-84 Plus CE python.
    The main diference with the normal print is that 
    this one prints the promt by separating lines each 32 characteres.
    The purpose for this is that TI screens shows 32 characteres and 
    we want to orginize each prompt for more readability when using the program.
    
    """
    words = prompt.split()
    formatted = ""
    line = ""

    for word in words:
        if len(line) + len(word) + 1 <= lineLength:
            line += word + " "
        else:
            formatted += line.rstrip() + "\n"
            line = word + " "
    
    # Agrega la última línea
    formatted += line.rstrip()
    print(formatted)
    return formatted


def errorDetection(errorNumber):

    dc()
    print("[==============================]")
    print("ERROR!!! ")

    if errorNumber == 101:
        print32("> [MENU]#101: You have entered an invalid or non-existent option.")

    elif errorNumber == 102:
        print32("> [MENU]#102: You are required to enter integer value to navigate the menus.")


    elif errorNumber == 201:
        print("> [OPERATION]#201: Your enter a invalid value type for this operation.")

    elif errorNumber == 202:
        print32("> [OPERATION]#202: You entered a value below of the aceptable range for this operation.")

    elif errorNumber == 203:
        print32("> [OPERATION]#203: Your entered a value over of the aceptable range for this operation.")
    

    elif errorNumber == 301:
        print32("> [Z_TEST]#301: Success Condition: We need sample sizes times p hat ≥ 10.")

    elif errorNumber == 302:
        print32("> [Z_TEST]#302: Failure Condition: We need sample sizes times 1 - p hat ≥ 10.")

    
    else:
        pass



    input("Press ENTER to continue...")
    dc()
    return errorNumber

def wantGoToMenu():

    while True:
        print("Go to main manu? ")
        print("[1] - Yes \n[2] - No")

        goToMenu = checkMenuOptions(1, 2)
    

        if goToMenu == 1:
            return True
        
        return False


def isSpecificInput(prompt: str, valueType="float", minimumValueForNum=None, maximumValueForNum=None):

    if valueType == "str":
        inputValue = input(prompt)
        return inputValue

    elif valueType == "int":
        try:
            inputValue = int(input(prompt))
        except:
            errorDetection(201)
            return None
        
        if minimumValueForNum != None: 
            if inputValue < minimumValueForNum:
                errorDetection(202)
                return None
        
        if maximumValueForNum != None:
            if inputValue > maximumValueForNum:
                errorDetection(203)
                return None
        
        return int(inputValue)

    elif valueType == "float":
        try:
            inputValue = float(input(prompt))
        except:
            errorDetection(201)
            return None
        
        if minimumValueForNum != None:
            if inputValue < minimumValueForNum:
                errorDetection(202)
                return None
        
        if maximumValueForNum != None:
            if inputValue > maximumValueForNum:
                errorDetection(203)
                return None
        
        return float(inputValue)

def checkMenuOptions(minimumValue=0, maximumValue=10):
    
    try:
        menuOption = int(input(">>> "))
        
    except:
        errorDetection(102)
        return None
    
    if menuOption < minimumValue or menuOption > maximumValue:
        errorDetection(101)
        return None
    
    return menuOption
        
    


