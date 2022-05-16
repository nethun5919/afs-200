
step1 = input("Can you guess the secret occupation?")
print(step1)

word ="secretary" 

wordBoard = ["_","_","_","_","_","_","_","_","_"]
print(wordBoard)

mylist = []

def snowBoard ():
   print(wordBoard)    

def checkGuess(guessedLetter):
    foundRec = []
    position = 0
    for letter in word:
        if letter == guessedLetter: 
            foundRec.append(position)
        position += 1
    print(foundRec)

checkGuess ("e")