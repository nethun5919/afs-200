


word ="secretary" 

wordBoard = ["_","_","_","_","_","_","_","_","_"]
print(wordBoard)

mylist = []
win = False
lives = 5 

def snowBoard ():
   print(wordBoard)    

def checkGuess(guessedLetter, lives):
    print(lives)
    foundRec = []
    position = 0
    for letter in word:
        if letter == guessedLetter: 
            foundRec.append(position)
            print(position)
        position += 1
    print(foundRec)
    if (len(foundRec)<1):
        lives -= 1
        return lives
    else:

        for index in foundRec:
            wordBoard[index] = guessedLetter

        counter = 0
        for blank in wordBoard:
            if blank !="_":
                counter +=1
        
        if counter == len(word):
           return True
        else:
            return False

print("Can you guess the secret occupation?")
while (win == False and lives>0):

    guess = input("Guess a letter, ")
    print(guess)

    result = checkGuess (guess,lives)
    print(type(result))
    if type(result) is int:
        lives = result
    else:
        win = result 
       
    snowBoard ()  

print(lives, win)
if win ==True:
    print('Winner.')
else:
    print('You loose.')