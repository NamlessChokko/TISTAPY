import TISTAUTI as UT
import TISTAPY as TP


def mainMenu():
    
    while True:
        print("\nWelcome to TISTAPY - Statistics on TI-84 CE with Python")
        print("Select an option: ")
        print("[1] - Info")
        print("[2] - Z-Test")
        print("[3] - T-Test")
        print("[4] - None")
        print("[5] - None")
        print("[6] - None")
        print("[0] - Exit the program")

        menuOption = UT.checkMenuOptions(0, 6)
        
        if menuOption == None:
            continue

        elif menuOption == 0:
            break

        elif menuOption == 1:
            
            infoTPMenu()

        elif menuOption == 2:
            
            z_testMenu()
        
        elif menuOption == 3:

            t_testMenu()


def infoTPMenu ():

    while True:
        print("\n[>>Info<<]")
        print("TISTAPY is a python module specifically for TI calculators.")

        if UT.wantGoToMenu():
            break


def z_testMenu():

    while True:
        print("\n[>>Z-Test<<]")
        print("Select an option: ")
        print("[1] - Calculate Z-Score for Z-Test")
        print("[2] - Info")
        print("[0] - Go to main menu")

        optionMenu = UT.checkMenuOptions(0, 2)

        if optionMenu == None:
            continue


        if optionMenu == 1:

            sampleProportion = UT.isSpecificInput("Enter your sample proportion: ", "float", 0, 1)
            if sampleProportion == None:
                continue

            nullProportion = UT.isSpecificInput("Enter your null proportion: ", "float", 0, 1)
            if nullProportion == None:
                continue

            sampleSize = UT.isSpecificInput("Enter your sample size: ", "int")
            if sampleSize == None:
                continue

            z_score = TP.z_test(sampleProportion, nullProportion, sampleSize)

            print("Your z-score for this Hypotesis is: ", z_score)



        elif optionMenu == 2:
            print("Z-test is use to determine hypotesis about normal distributions")

        else:
            return 
        

def t_testMenu():
    
    while True:
        print("\n[>>T-Test<<]")
        print("Select an option: ")
        print("[1] - Calculate T-Score for T-Test")
        print("[2] - Info")
        print("[0] - Go to main menu") 

        optionMenu = UT.checkMenuOptions(0, 2)

        if optionMenu == None: 
            continue

        if optionMenu == 1:
            sampleMean = UT.isSpecificInput("Enter your sample mean: ")
            if sampleMean == None:
                continue
        
            nullPopulation = UT.isSpecificInput("Enter your null population: ")
            if nullPopulation == None:
                continue

            sampleStandardDeviation = UT.isSpecificInput("Enter your sample standard deviation: ")
            if sampleStandardDeviation == None:
                continue

            sampleSize = UT.isSpecificInput("Enter your sample size: ", "int")
            if sampleSize == None:
                continue

            t_score = TP.t_test(sampleMean, nullPopulation, sampleStandardDeviation, sampleSize)
            print("Your T-Score is: ", t_score)

        elif optionMenu == 2:
            print("T-test is use to determine main hypotesis about a normal distribution.")
        
        else:
            return

