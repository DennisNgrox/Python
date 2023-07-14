def nome(nome):
    return f'Oi {nome}'

lista = ['a', 'b', 'c']

nomes = list(map(nome, lista)) ## função map adiciona os valores da lista na função "nome"

print(nomes)
