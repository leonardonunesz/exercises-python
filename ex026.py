#A program that reads a phrase and show: how many times 'A' appears, what position it appears the first time, what position it appears the last time
phrase = str(input('Enter a phrase: '))
ta = phrase.upper().count('A')
fta = phrase.upper().find('A')
lta = phrase.upper().rfind('A')

print('How many times it appears: {} \nWhat position appears the first time: {} \nWhat position appears the last time: {}'.format(ta, fta, lta))