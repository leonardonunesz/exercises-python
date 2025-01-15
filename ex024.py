#a program that reads a name of a city, and say if begin or not with 'SANTO'.
cityname = input('Enter a city name: ')
citynamesplit = cityname.split()
print('begins with SANTO is: {}'.format('SANTO' in citynamesplit[0].upper()))