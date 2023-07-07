import random


lista = list()
dic = dict()


for i in range(0, 4):
    jogador = random.randrange(1,7)
    print(f'jogador {i} tirou o valor {jogador}')
    number_jogador = str(i)
    dic['name'] = str(f'jogador {i}')
    dic['dado'] = jogador
    lista.append(dic.copy())

jogador_list = list()
number = list()

for e in lista:
    number.append(int(e['dado']))
    jogador_list.append(e['name'])
    
number.sort()

a = number[3]

for x in lista:
    b = int(x['dado'])
    c = x['name']
    if a == b:
        print(f'-----GANHADOR----')
        print(f'{c} com o valor {b}')
