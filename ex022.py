#make a program that reads a fullname of someone and show: The name with every word in UPPER, LOWER, how many letters in all (without considering spaces), how many letters has the first name
fullname = input('Enter a full name: ')
fullnamesplit = fullname.split()
firstname = fullnamesplit[0]
fullnamejoin = ''.join(fullnamesplit)
print('In uppercase: {}\nIn lowercase: {}\nHow many letters in full name: {}\nHow many letters the first name: {}'.format(fullname.upper(), fullname.lower(), len(fullnamejoin), len(firstname)))