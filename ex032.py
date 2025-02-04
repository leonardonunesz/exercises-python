#A program that reads any year and show if it is a leap year
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Its a leap year')
else:
    print('It is not a leap year')