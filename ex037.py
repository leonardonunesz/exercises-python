#Read an int number and ask which conversion basis:     1 to binary     2 to octal    3 to hexadecimal
n = int(input('Digit a number: '))
cb = int(input('Digit a conversion basis(1 to binary 2 to octal 3 to hexadecimal): '))
if cb == 1:
    print('\033[33mThe conversion of {} to binary is {}.\033[m'.format(n, bin(n)[2:]))
elif cb == 2:
    print('\033[33mThe conversion of {} to octal is {}.\033[m'.format(n, oct(n)[2:]))
elif cb == 3:
    print('\033[33mThe conversion of {} to hexadecimal is {}.\033[m'.format(n, hex(n)))
else:
    print('\033[31mInvalid input\033[m')