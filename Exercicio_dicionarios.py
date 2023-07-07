lista = list()
dic = dict()


for i in range(0, 3):
    nome = str(input("Nome: "))
    media = float(input(f'Média de {nome}: '))

    dic['nome'] = nome
    dic['média'] = media

    if media < 5:
        reprovado = 'Reprovado'
        dic['Status'] = reprovado
        print(f'Nome é igual a {nome}')
        print(f'Média é igual a {media}')
        print(f'Situação igual a {reprovado}')

    else:
        aprovado = 'Aprovado'
        dic['Status'] = aprovado
        print(f'Nome é igual a {nome}')
        print(f'Média é igual a {media}')
        print(f'Situação igual a {aprovado}')

    lista.append(dic.copy(D))


print(lista)
