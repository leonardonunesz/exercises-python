#countdown to fireworks, from 10 to 1, with a second delay
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FIREWORKS!!!')