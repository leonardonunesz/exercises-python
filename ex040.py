#make a program that reads 2 grades of a student calculate and show the average
# below 5.0 reproved    between 5.0 and 6.9 recovery    above 7.0
n1 = float(input('Digit your first grade: '))
n2 = float(input('Digit your second grade: '))
m = (n1 + n2) / 2
if m < 5:
    print('Your final grade is {}. \033[35mYou reproved!'.format(m))
elif 5 >= m < 6.9:
    print('Your final grade is {}. \033[33mYou are in recovery!'.format(m))
else:
    print('Your final grade is {}. \033[32mYou passed! Congratulations!!'.format(m))