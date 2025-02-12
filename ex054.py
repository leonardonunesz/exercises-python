#Read birthday year from seven peoples. Show how many are not legal of age yet
from datetime import date
major = 0
minor = 0
actual = date.today().year
for person in range(1, 8):
    by = int(input('Digit your birthday year: '))
    year = actual - by
    if year > 21:
        major += 1
    else:
        minor += 1
print('{} of these people are of legal age'.format(major))
print('{} of these people are underage'.format(minor))
