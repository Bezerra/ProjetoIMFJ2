# author Pedro Albuquerque Bezerra
# student number 21900974

from floatationSolver import *
from springSolver import *

def main_menu():
    print("What problem do you want to solve?")
    print("1. Floatation")
    print("2. Springs")
    print("0. Exit")
    textIn = (input())

    # deals with wrong inputs
    while (textIn != "1" and textIn != "2" and textIn != "0"):
        print("Not recognized. Please input a valid command.")
        textIn = (input())

    # returns input to main program
    return int(textIn)

def main():
    while (True):
        textIn = main_menu()
        
        # case Floatation
        if (textIn == 1):
            floatSol = floatationSolver()
            floatSol.menu()
            floatSol.solve()
            followUp = floatSol.followUpMenu();
            while(followUp):
                floatSol.changeParameter(followUp)
                floatSol.solve()
                followUp = floatSol.followUpMenu()
        
        # case Spring
        elif (textIn == 2):
            springSol =  springSolver()
            springSol.menu()
            print("The spring would stretch to ", springSol.solve(), " meters")
            followUp = springSol.followUpMenu();
            while(followUp):
                springSol.changeParameter(followUp)
                print("The spring would stretch to ", springSol.solve(), " meters")
                followUp = springSol.followUpMenu();
        
        
        elif(textIn == 0):
            print("Exiting program...")
            exit()
        

if __name__ == "__main__":
    main()