word = 'calvin'
tries = 5
display= '_'* len(word)


game_over = False

while not game_over:
    print('you have' + str(tries) + 'remaining')
    print(display)
    guess = input('Please guess a letter:')

    i = 0
    if guess in word:
        while word.find(guess, i) != -1:
            i = word.find(guess, i)
        display= display[:1] + guess + display[i + 1]
        i +=1
    print('correct')

else:
    print('sorry, wrong guess.')

    print(display)
    game_over = True    
