#Write a program that makes the computer 'think' a number between 0 and 5 and ask for the user guess which number was chosen
#The program may write in the screen if the user loses or win
import random
rnumber = random.randint(0,5)
cnumber = int(input('Try to guess the number that I am thinking: '))
if cnumber == rnumber:
    print('The number was: {}'.format(rnumber))
    print('You guessed right!')
else:
    print('The number was: {}'.format(rnumber))
    print('You guessed wrong!')