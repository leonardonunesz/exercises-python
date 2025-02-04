#A program that ask how many Km of a trip. Calculate the ticket price, $0.50 per km until 200km and $0.45 for longer trip
kmT = float(input('How many Km did you travel? '))
if kmT < 200:
    tp = kmT * 0.50
    print('The ticket price is ${:.2f}'.format(tp))
else:
    tp = kmT * 0.45
    print('The ticket price is ${:.2f}'.format(tp))