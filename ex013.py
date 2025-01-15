#make an algorithm that reads a wage(salário) of a collaborator and show your new wage with an increase of 15%
wage = float(input('What is your salary? '))
newWage = (wage * 0.15) + wage
print('Your new salary is ${:.2f}'.format(newWage))