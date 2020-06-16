# author Pedro Albuquerque Bezerra
# student number 21900974

class floatationSolver:
    def menu(self):
        self.gravity = float(input("Gravity (m/s2): "))
        self.fluidDen = float(input("Fluid density (kg/m3): "))
        self.objDen = float(input("Object density (kg/m3): "))
        self.objVol = float(input("Object volume (m3): "))
        self.objSide = self.objVol ** (1/3)
        self.objMass = self.objVol * self.objDen
        
        

    def solve(self):
        forceGravity = self.gravity * self.objMass
        subVol = forceGravity / (self.fluidDen * self.gravity)
        self.solvedMessage(subVol)

    def followUpMenu(self):
        print("\nChange parameter?")
        print("1. Gravity")
        print("2. Fluid density")
        print("3. Object density")
        print("4. Object volume")
        print("5. Object mass")
        print("0. Back to main menu")
        textIn = input()

        # deals with wrong inputs
        # this was the easiest way to also catch  the user entering letters instead of numbers
        while (textIn != "1" and textIn != "2" and textIn != "3" and textIn != "4" and textIn != "5" and textIn != "0"):
            print("Not recognized. Please input a valid command.")
            textIn = (input())

        return int(textIn)

    def changeParameter(self, paraID):
        if (paraID == 1):
            self.gravity = float(input("Gravity: "))
        elif (paraID == 2):
            self.fluidDen = float(input("Fluid density: "))
        elif (paraID == 3):
            self.objDen = float(input("Object density: "))
            self.objMass = self.objVol * self.objDen
        elif (paraID == 4):
            self.objVol = float(input("Object volume: "))
            self.objSide = objVol ** 1/3
            self.objMass = self.objVol * self.objDen
        elif (paraID == 5):
            self.objMass = float(input("Object mass: "))
            self.objVol = self.objMass / self.objDen
            self.objSide = objVol ** 1/3

    def solvedMessage(self, subVol):
        if(subVol >= self.objVol):
            print("The object would sink")
        else:
            
            # submerged volume = area * submerged distance
            area = self.objSide * self.objSide
            subDist = subVol / area
            
            # center is half the side
            centerDist = self.objSide / 2
            
            # output is distance from center. Positive means center is above, negative means it is below
            subDist = centerDist - subDist
            if(subDist >= 0):
                print("The object would float, with the center ", subDist, " meters above water")
            else:
                print("The object would float, with the center ", subDist, " meters below water")