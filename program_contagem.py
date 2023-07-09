from operator import neg

def linha(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


def contador(inicio, fim, passo):
    if inicio > fim:
        linha(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        passo = neg(passo)
        for e in range(fim, inicio, passo * -1):
            print(e, end=' ')
    else:
        passo = passo * 1
        linha(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            
        

linha('RESULTADO')

inicio = int(input('Inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))

contador(1, 10, 1)
print('')
contador(10, 0, 2)
print('')
contador(inicio, fim, passo)
