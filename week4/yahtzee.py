
import random

class Dice: 
    sides = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']


    def __init__(self, sides = 6):
        self.numOfSides = sides
        self.numValue = 1


    def roll(self):
        self.numValue = random.randint(1,self.numOfSides)
        return self.numValue

    def getnumOfSides(self):
        return self.numOfSides

    def getCurrentSideUp(self):
        return self.numValue

    def showDiceFace(self):
        print(f'{Dice.sides [self.getCurrentSideUp()-1]} {self.getCurrentSideUp()}', end= "")

def playYahtzee():
    myDice = [Dice(),Dice(),Dice(),Dice(),Dice(),Dice()]

    for dice in myDice:
        dice.roll()
        dice.showDiceFace()
    yahtzee = all(dice.getCurrentSideUp() == myDice[0].getCurrentSideUp()for dice in myDice)
    if yahtzee:
        print("\nYAHTZEE")

playYahtzee()