#read 6 int numbers and show the sum of the even number, discard the odds
total = 0
for c in range(6):
    n = int(input('Digit a value: '))
    if n % 2 == 0:
        total += n
print('Sum of even numbers: {}'.format(total))