lista = dict()

# Add dados do dic

lista['nome'] = 'dennis'
lista['idade'] = 25

# Deletar dados do dic
del lista['nome']

# Print lista
print(lista)


dados = {
    'titulo': 'Star wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}


teste = {
    'titulo': 'Star wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(dados['titulo'])

# para pegar as chaves

print(dados.keys()) #chaves
print(dados.values()) # valores
print(dados.items()) # keys e values

locadora = list()

locadora.append(dados) 
locadora.append(teste)

print(locadora[1]['ano'])
