valores = [
    1000,
    2000,
    3000,
    4000
]

def somar(number):
   number += number
   return number


resultado = list(map(somar, valores)) # or filter

dicionario = dict()
lista = list()

dicionario['valor'] = resultado


for i in range(len(valores)):
   dicionario['valor'] = valores[i]
   lista.append(dicionario)

print(lista)
