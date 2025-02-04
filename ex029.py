#Write a program that reads the car velocity, if exceed the 80km/h limiter, show a messenger saying they were fined, the fine cost $7.00 per km over the limit
kmCar = float(input('How many Km are you driving? '))
fine = (kmCar - 80) * 7
if kmCar > 80:
    print('You were fined in ${:.2f}!'.format(fine))
else:
    print('You were in the limit!! Keep going!')