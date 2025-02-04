#only the sum of odd and multiples of 3, from 1 to 500
s = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print(s)