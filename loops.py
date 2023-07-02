# Contagem regressiva em Python:
import time

tempo = int(input('Digite o tempo: '))

for i in range(tempo, 0, -1):
    time.sleep(1)
    print(i)
print('Fogos estourando...')

# Mostrar todos números pares de 1 á 50

for c in range(0, 51, 2):
    print(c, end=' ')


# while

c = 1

while c < 10:
    print(c)
    c += 1


# Exercicio de validação de Sexo:
sexo = str(input('Qual seu sexo: '))

while sexo not in 'MmFf':
    sexo = str(input('Qual seu sexo: '))
