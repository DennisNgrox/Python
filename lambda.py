#lambda
valor = [1, 2, 3, 4]

res = [ valor * 10 for valor in valor ]


# not lambda
valor = [1, 2, 3, 4]

def multiplicar(valor):
    valor = valor * 10
    return valor


resultado = list(map(multiplicar, valor))

print(resultado)
