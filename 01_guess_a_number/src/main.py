from random import randrange

def guessANumber(guess):

    if guess > 10:
        print('Error! Number too big')
        return
    elif guess < 1:
        print('Error! Number too small')
        return

    randomNumber = randrange(10)
    if guess == randomNumber:
        print('Win')
    else:
        print('Lose')
        print('Number is ' + str(randomNumber))

input = int(input('>>> Enter a number between 1 and 10 to guess: '))
guessANumber(input)