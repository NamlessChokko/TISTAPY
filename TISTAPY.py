import math  
from ti_system import disp_clr as dc


def z_test(p_sample: float, p_null: float, sampleSize: int) -> float:
    # Conditions to check if the sample size is large enough for a Z-test
    conditionsForZTest = [(sampleSize * p_sample) < 10, sampleSize * (1 - p_sample) < 10]

    # If either of the conditions is violated (n*p or n*(1-p) should be >= 10), the test can't be executed
    if conditionsForZTest[0] or conditionsForZTest[1]:
        # Print specific failure conditions
        if conditionsForZTest[0]:
            errorDetection(301) 
        if conditionsForZTest[1]:
            errorDetection(302)
        return None  # Return 0 to indicate failure to execute test

    # Calculate the numerator (difference between sample proportion and null proportion)
    numerator = p_sample - p_null
    # Calculate the denominator (standard error of the sample proportion)
    denominator = math.sqrt((p_null * (1 - p_null)) / sampleSize)

    # Return the Z-test statistic, which is the ratio of the numerator and denominator
    return numerator / denominator

def t_test(x_bar: float, mu_null: float, s_sample: float, sampleSize: int) -> float:
    # Conditions to determine whether the sample size is appropriate for a t-test
    conditionsForTTest = [sampleSize < 15, sampleSize >= 15 and sampleSize < 40]

    # Check for the condition when sample size is less than 15
    if conditionsForTTest[0]:
        print32("Sample Size < 15 -- Do not use t-methods if there is strong skewness or outliers.")
    # Check for the condition when sample size is between 15 and 40
    elif conditionsForTTest[1]:
        print32("15 <= Sample Size < 40 -- t-methods should not be used in the presence of outliers or strong skewness.")

    # Calculate the numerator (difference between sample mean and null hypothesis mean)
    numerator = x_bar - mu_null
    # Calculate the denominator (standard error of the sample mean)
    denominator = s_sample / (math.sqrt(sampleSize))

    # Return the t-test statistic, which is the ratio of the numerator and denominator
    return numerator / denominator


def erf(x):
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911
        
        t = 1 / (1 + p * abs(x))
        return 1 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)

        
def normalCDF_from_z(z_score, hypo: int = 0, mean: float = 0, standard_deviation: float = 1) -> float:

    cdf = 0.5 * (1 + erf(z_score))

    if hypo == 1:
        return cdf
    
    elif hypo == 2:
        return 1 - cdf
    
    elif hypo == 0:
        return 2 * min(cdf, 1 - cdf)
    
    else:
        return cdf

#==========================================================================================================
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
    

    formatted += line.rstrip()
    print(formatted)
    return formatted 


def errorDetection(errorNumber: int) -> str:

    dc()
    print("[==============================]")
    print("ERROR!!! ")

    
    errorList= {101: "> [MENU]#101: You have entered an invalid or non-existent option.",
                102: "> [MENU]#102: You are required to enter integer value to navigate the menus.",
                103: "> [MENU]#103: This option is under maintenance.",
                201: "> [OPERATION]#201: You entered a invalid type for this operation.",
                202: "> [OPERATION]#202: You entered a value below of the aceptable range for this operation.",
                203: "> [OPERATION]#203: Your entered a value over of the aceptable range for this operation.",
                301: "> [Z_TEST]#301: Success Condition: We need sample sizes times p hat >= 10.",
                302: "> [Z_TEST]#302: Failure Condition: We need sample sizes times 1 - p hat >= 10.",
                401: "> [HYP_TEST_P]#401: You entered a invalid value for the hypotesis. "}
    
    

    print32(errorList[errorNumber])
    input("\nPress Enter to continue...")
    dc()
    return errorNumber


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

def checkMenuOptions(maximumValue: int=3, errorReturnForType: int = 102,errorReturnForRange: int = 101):
    

   
    try:
        menuOption = int(input(">>> "))
        
    except:
        errorDetection(errorReturnForType)
        return None
    
    if menuOption < 0 or menuOption > maximumValue:
        errorDetection(errorReturnForRange)
        return None
    
    return menuOption

#===========================================================================================================
def menu1 ():
    
    while True:
        dc()
        print("[==============================]")
        print("Welcome to TISTAPY")
        print32("Statistics on TI-84 CE with Python")
        print("Select an option: ")
        print("[1] - Info")
        print("[2] - Z-Test")
        print("[3] - T-Test")
        print("[4] - Next Page")
        print("[0] - Exit the program")

        menuOption = checkMenuOptions(6)
        
        
        if menuOption == None:
            continue

        elif menuOption == 0:
            dc()
            print("Thank for using the program.")
            break

        elif menuOption == 1:
            
            infoTPMenu()

        elif menuOption == 2:
            
            z_testMenu()
        
        elif menuOption == 3:

            t_testMenu()

        elif menuOption == 4:
            menu2()

def menu2 ():

    while True:
        dc()
        print("[==============================]")
        print("         [>>Page 2<<]")
        print("Select an option: ")
        print("[1] - Hypo Test for Proportion")
        print("[2] - NONE")
        print("[3] - NONE")
        print("[4] - NONE")
        print("[5] - NONE")
        print("[6] - NONE")
        print("[0] - Go Back")

        menuOption = checkMenuOptions(7)

        if menuOption == 0:
            return
        
        elif menuOption == 1:

            hy_test_for_proportion_Menu()

        elif menuOption == 2:
            errorDetection(103)


        elif menuOption == 3:
            errorDetection(103)

        
        elif menuOption == 4:
            errorDetection(103)


        elif menuOption == 5:
            errorDetection(103)


        elif menuOption == 6:
            errorDetection(103)
    

def infoTPMenu ():

    while True:
        dc()
        print("[==============================]")
        print("          [>>Info<<]")
        print("TISTAPY is a python module ")
        print32("specifically for TI calculators.")
        print("Go to main menu?")
        print("[0] - Yes")
        print("[1] - No")
        isExit = checkMenuOptions(1)
        

        if isExit == 0:
            return
        
        
def z_testMenu():

    while True:
        dc()
        print("[==============================]")
        print("         [>>Z-Test<<]")
        print("Select an option: ")
        print("[1] - Calculate Z-Score for ")
        print("Z-Test")
        print("[2] - Info")
        print("[0] - Go back")

        optionMenu = checkMenuOptions(2)

        if optionMenu == None:
            continue


        if optionMenu == 1:

            dc()
            sampleProportion = isSpecificInput("Sample proportion: ", "float", 0, 1)
            if sampleProportion == None:
                continue

            nullProportion = isSpecificInput("Null proportion: ", "float", 0, 1)
            if nullProportion == None:
                continue

            sampleSize = isSpecificInput("Sample size: ", "int")
            if sampleSize == None:
                continue

            z_score = z_test(sampleProportion, nullProportion, sampleSize)

            if z_score == None:
                continue

            dc()
            print32("Your z-score for this Hypotesis is: ")
            print(z_score)
            input("\nPress Enter to continue...")



        elif optionMenu == 2:
            print32("Z-test is use to determine hypotesis about normal distributions")
            input("\nPress Enter to continue...")

        else:
            return 
        
def t_testMenu():
    
    while True:
        dc()
        print("[==============================]")
        print("         [>>T-Test<<]")
        print("Select an option: ")
        print("[1] - Calculate T-Score for")
        print("T-Test")
        print("[2] - Info")
        print("[0] - Go back") 

        optionMenu = checkMenuOptions(2)

        if optionMenu == None: 
            continue

        elif optionMenu == 0:
            break

        elif optionMenu == 1:
            dc()
            sampleMean = isSpecificInput("Sample mean: ")
            if sampleMean == None:
                continue
        
            nullPopulation = isSpecificInput("Population Mean: ")
            if nullPopulation == None:
                continue

            sampleStandardDeviation = isSpecificInput("Sample standard deviation: ")
            if sampleStandardDeviation == None:
                continue

            sampleSize = isSpecificInput("Sample size: ", "int", 2)
            if sampleSize == None:
                continue

            dc()
            t_score = t_test(sampleMean, nullPopulation, sampleStandardDeviation, sampleSize)
            print("\nYour T-Score is for this hypotesis is: ")
            print(t_score)
            input("\nPress Enter to continue...")

        elif optionMenu == 2:
            print32("T-test is use to determine main hypotesis about a normal distribution.")
            input("\nPress Enter to continue...")
        

def hy_test_for_proportion_Menu():

    while True:
        dc()
        print("[==============================]")
        print(" [>>Hypo Test For Proportion<<]")
        print("Select an option: ")
        print32("[1] - Calculate hypotesis test for proportion")
        print("[2] - Info")
        print("[0] - Go back")

        optionMenu = checkMenuOptions(2)

        if optionMenu == None:
            continue

        elif optionMenu == 0:
            return

        elif optionMenu == 1:
            dc()

            print("Select your Hypotesis: ")
            print("[0] - Two-tailed test")
            print("[1] - Left-tailed test")
            print("[2] - Right-tailed test")
    
            test = checkMenuOptions(2, 102, 401)
            if test == None:
                continue

            nullProportion = isSpecificInput("Null Hypotesis: ", "float", 0, 1)
            if nullProportion == None:
                continue

            significantLevel = isSpecificInput("Significant Level: ", "float", 0.00)
            if significantLevel == None:
                continue

            sampleSize = isSpecificInput("Sample Size: ", "int")
            if sampleSize == None:
                continue

            sampleProportion = isSpecificInput("Sample Proportion: ", "float", 0.00, 1.00)
            if sampleProportion == None:
                continue

            dc()
            
            z_score = z_test(sampleProportion, nullProportion, sampleSize)
            print("The Z-Score for this hypothesis is : ", z_score)

            proportion = normalCDF_from_z(z_score, test)
            print("The proportion of this hypothesis is: ", proportion)

            acceptHypothesis = proportion > significantLevel

            if acceptHypothesis:
                print("The Hypothesis is acepted")
                input("Press Enter to continue...")
                continue

            print("The Hypotesis is rejected")
            input("Press Enter to continue...")
            continue


        elif optionMenu == 2:
            print32("Info")
            input("Press Enter to continue...")

#============================================================================================================
def main ():
    menu1 ()

main()

