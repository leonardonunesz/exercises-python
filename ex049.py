#multiplication table with for

n = int(input('Digit a number: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
