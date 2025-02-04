#a program that reads the first term of an arithmetic progression and the reason. In the end, show the firsts 10 terms of this progression
pt = int(input('Digit the first term of an AP: '))
r = int(input('Digit the reason: '))
for c in range(10):
    term = pt + c * r
    print(term)
print('END')