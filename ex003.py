cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'cinza': '\033[35m'
}

n1 = int(input('Digit a number: '))
n2 = int(input('Digit another number: '))
s = n1 + n2
print('The sum of {}{}{} and {}{}{} is {}{}{}'.format(cores['verde'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['amarelo'], s, cores['limpa']))