#make a rock paper or scissor game
import random
player = input('Choose rock paper or scissor: ')
choices = ['rock', 'paper', 'scissor']
computer = random.choice(choices)

win = 'You win!'
lose = 'You lose!'
tie = 'It\'s a tie!'
vs = 'player choose: {} VS computer choose: {}!!'.format(player, computer)

if player == computer:
    print(vs)
    print(tie)
elif player == 'rock':
    if computer == 'scissor':
        print(vs)
        print(win)
    elif computer == 'paper':
        print(vs)
        print(lose)
elif player == 'scissor':
    if computer == 'paper':
        print(vs)
        print(win)
    elif computer == 'rock':
        print(vs)
        print(lose)
elif player == 'paper':
    if computer == 'scissor':
        print(vs)
        print(lose)
    elif computer == 'rock':
        print(vs)
        print(win)
print('End of the game!')