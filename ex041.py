#read the birtdate year of an athlete and show your category, according your age:
# 9: kid  14: childish  19: junior  20: senior  above: master
year = int(input('Digit your birthdate year: '))
yearold = 2025 - year
if yearold <= 9:
    print('kid')
elif yearold <= 14:
    print('childish')
elif yearold <= 19:
    print('junior')
elif yearold <= 20:
    print('senior')
else:
    print('master')
