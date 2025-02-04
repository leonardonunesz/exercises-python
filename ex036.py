#write a program that approve a bank loan to buy a house. The program should ask the house value, the salary of the buyer and in how many years they will pay.
#calculte the value of the monthly installment, knowing they cant exceed 30% of the salary or the loan will be negated
house = float(input('What is the house price? '))
salary = float(input('What is the salary? '))
year = float(input('How many years you pretend to pay? '))
monthlyi = house / (year * 12)
print('To pay a \033[1;34m${:.2f}\033[m house in \033[1;34m{:.2f}\033[m years\nThe monthly installment will be \033[1;34m${:.2f}\033[m'.format(house, year, monthlyi))

if salary * 0.30 < monthlyi:
    print('\033[1;31mYou cant finance this house, I am sorry!\033[m')
else:
    print('\033[1;32mThe loan was approved!!\033[m')