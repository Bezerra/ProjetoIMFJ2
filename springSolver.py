# author Pedro Albuquerque Bezerra
# student number 21900974

class springSolver:
    def menu(self):
        self.gravity = float(input("Gravity (m/s2): "))
        self.objMass = float(input("Object mass (kg): "))
        self.springRest = float(input("Spring length in rest (m): "))
        self.springConst = float(input("Spring constant (N/m): "))
        
        

    def solve(self):
        self.springConst *= -1
        forceGravity = self.gravity * self.objMass
        springStretch = forceGravity / self.springConst
        springStretch += self.springRest
        return springStretch

    def followUpMenu(self):
        print("\nChange parameter?")
        print("1. Gravity")
        print("2. Object mass")
        print("3. Spring length in rest")
        print("4. Spring constant (N/m)")
        print("0. Back to main menu")
        textIn = input()

        # deals with wrong inputs
        # this was the easiest way to also catch  the user entering letters instead of numbers
        while (textIn != "1" and textIn != "2" and textIn != "3" and textIn != "4" and textIn != "0"):
            print("Not recognized. Please input a valid command.")
            textIn = (input())

        return int(textIn)

    def changeParameter(self, paraID):
        if (paraID == 1):
            self.gravity = float(input("Gravity: "))
        elif (paraID == 2):
            self.objMass = float(input("Object mass: "))
        elif (paraID == 3):
            self.springRest = float(input("Spring length in rest: "))
        elif (paraID == 4):
            self.springConst = float(input("Spring constant: "))


