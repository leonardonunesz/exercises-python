#A program that reads a full name, and show the first name and the last name separately     ex: Ana Maria de Souza  First = Ana Last = Souza
fullname = input("Enter your full name: ")
fullnamesplit = fullname.split()
firstname = fullnamesplit[0]
lastname = fullnamesplit[-1]
print('The first name is: {} \nThe last name is: {}'.format(firstname, lastname))