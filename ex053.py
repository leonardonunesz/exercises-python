#A program that reads a phrase and tells if it's a palindrome
phrase = str(input('Digit a phrase: ')).strip().upper()
word = phrase.split()
wordt = ''.join(word)
inverse = ''

for letter in range(len(wordt)-1, -1, -1):
    inverse += wordt[letter]
print('The word is: \033[32m{}\033[m the inverse is: \033[35m{}\033[m'.format(wordt, inverse))
if inverse == wordt:
    print('It\'s a palindrome.')
else:
    print('It is not a palindrome.')