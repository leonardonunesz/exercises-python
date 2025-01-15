#A program that reads a number between 0 and 9999 and show on screen each digit separate        ex: 1834    unit: 4 dozen: 3 hundred: 8 thousand: 1
n = input('Enter a number with 4 digits: ')
print('Unit: {} \nDozen: {} \nHundred: {} \nThousand: {}'.format(n[3],n[2],n[1],n[0]))
