#Write a program that asks how many kilometers traveled by a rented car and how many days it was rented
#Calculate how much to pay, knowing that the car costs $60 per day and $0.15 per Km traveled
km = float(input('How many kilometers you traveled? '))
days = float(input('How many days the car was rented? '))
kmT = km * 0.15
daysT = days * 60
Total = kmT + daysT
print('Knowing you have to pay ${:.2f} for kilometers and ${:.2f} for days\nYou have to pay in total ${:.2f}'.format(kmT, daysT, Total))