


word ="secretary" 

wordBoard = ["_","_","_","_","_","_","_","_","_"]
print(wordBoard)

mylist = []

def snowBoard ():
   print(wordBoard)    

def checkGuess(guessedLetter, lives):
    foundRec = []
    position = 0
    for letter in word:
        if letter == guessedLetter: 
            foundRec.append(position)
            print(position)
        position += 1
    print(foundRec)
    if (len(foundRec)<1):
        lives = lives-1
        
    for index in foundRec:
        wordBoard[index] = guessedLetter

    print(wordBoard)
    print(lives)
           
win = False
lives = 5 

print("Can you guess the secret occupation?")
while (win == False and lives>1):

    step1 = input("Guess a letter, ")
    print(step1)

    checkGuess (step1, lives)

