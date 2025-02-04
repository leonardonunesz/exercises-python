#a program that calculate a value to be paid for a product, considering your normal price and your condition payment
#in money/bank check: 10% discount      card: 5% discount       2x in card: normal price   3x or more in card: 20% fees

product = float(input('Digit the product value: '))
money = input('You will pay in money or bank check? Y/N \n')

if money.upper() == 'Y':
    total = product - (product * 0.10)
    print('Your total is:', total)
elif money.upper() == 'N':
    card = input('You will pay in card? Y/N \n')
    if card.upper() == 'Y':
        parcel = input('You want to parcel? Y/N \n')
        if parcel.upper() == 'N':
           total = product - (product * 0.05)
           print('Your total is:', total)
        else:
            timescard = input('How many times do you want to pay in installments? \n' )
            if timescard.lower() == '2':
               total = product
               print('Your total is:', total, '\nYou can pay in 2x of', total/2)
            else:
                total = product + (product * 0.20)
                print('Your total is:', total)
    else:
        print('Error!!')
