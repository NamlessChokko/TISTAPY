

def errorDetection(errorNumber):
    print("[==============================]")
    print("ERROR!!! ")

    if errorNumber == 101:
        print("> [MENU]#101 - You have entered an invalid or non-existent option.")

    elif errorNumber == 102:
        print("> [MENU]#102 - You are required to enter integer values ​​to navigate the menus.")


    elif errorNumber == 201:
        print("> [OPERATION]#201 - Your enter a invalid value type for this operation.")

    elif errorNumber == 202:
        print("> [OPERATION]#202 - You entered a value below of the aceptable range for this operation.")

    elif errorNumber == 203:
        print("> [OPERATION]#203 - Your entered a value over of the aceptable range for this operation.")
    

    elif errorNumber == 301:
        print("> [Z_TEST]#301 - Success Condition: We need 𝑛𝑝̂ ≥ 10.")

    elif errorNumber == 302:
        print("> [Z_TEST]#302 - Failure Condition: We need 𝑛(1 − 𝑝̂) ≥ 10.")

    
    else:
        pass

    print("Please try again.")
    return errorNumber

def wantGoToMenu():

    while True:
        print("Go to main manu? ")
        print("[1] - Yes \n[2] - No")

        goToMenu = checkMenuOptions(1, 2)
    
        if goToMenu == None:
            continue
        elif goToMenu == 1:
            return True
        elif goToMenu == 2:
            return None

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
        
    


