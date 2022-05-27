
import random

class dice: 
    sides = [1,2,3,4,5,6,7,8,9]

def __int__(self, sides = 6):
    self.numOfSides = sides
    self.currentSideUp= 1


def roll(self):
    self.currentSideUp= random.randint(1,self.nomOfSides)
    return self.numOfSides

def getNumOfSides(self):
    return self.numOfSides

def getCurrentSideUp(self):
    return self.currentSideUp

def showDiceFace(self):
    print(f'{dice.sides [self.getCurrentSideUp()]} {self.getCurrentSideUp()}', end= "")

def PlayYahtzee():
    myDice = {dice(),dice(),dice(),dice(),dice(),dice()}

    for dice in myDice:
        dice.roll()
        dice.showDiceFace()


yahtzee = all(dice.getCurrentSideUp() == myDice[0].getCurrentSideUp()for dice in myDice)

if yahtzee:
    print("\nYAHTZEE")

playYahtzee()