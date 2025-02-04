#Write a program that ask the salary of a coworker and calculate an increase
#For salary superiors of $1.250.00, calculate an increase of 10%        for lower or equal wages an increase of 15%

wage = float(input("Enter your wage: "))

if wage <= 1250:
    iwage = (wage * 0.15) + wage
    print("Your new wage is: ${:.2f}".format(iwage))
else:
    iwage = (wage * 0.10) + wage
    print("Your new wage is: ${:.2f}".format(iwage))