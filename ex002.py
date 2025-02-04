cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    }
name = input("Enter your name: ")
print('{}Welcome{} {}back{} {}{}{}!'.format(cores['verde'], cores['limpa'], cores['ciano'], cores['limpa'], cores['roxo'], name, cores['limpa']))