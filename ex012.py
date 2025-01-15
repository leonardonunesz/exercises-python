#make an algorithm that reads a price and show a product with 5% of discount
price = float(input('What is the price of the product? '))
discount = price * 0.05
total = price - discount
print('The product price is ${:.2f}'.format(total))