from functools import reduce

lista = [1, 2, 3, 4, 5, 6]

def soma(valor, valor1):
    s = valor + valor1
    return s

res = reduce(soma, lista)

print(res)

# output: 21
# reduce trata os valores da seguinte forma:
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21
# sempre armazenado resultado e prosseguindo na função
