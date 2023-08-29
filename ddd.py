ddd = [
    {
      "ddd": 61,
      "Destination": "Brasilia"
    },
        {
      "ddd": 71,
      "Destination": "Salvador"
    },
        {
      "ddd": 11,
      "Destination": "Sao Paulo"
    },
        {
      "ddd": 21,
      "Destination": "Rio de Janeiro"
    },
        {
      "ddd": 32,
      "Destination": "Juiz de Fora"
    },
        {
      "ddd": 19,
      "Destination": "Campinas"
    },
        {
      "ddd": 27,
      "Destination": "Vitoria"
    },
        {
      "ddd": 31,
      "Destination": "Belo Horizonte"
    }
]


value = int(input())

lista = []
for i in range(len(ddd)):
    lista.append(ddd[i]["ddd"])

if value not in lista:
    print("DDD nao cadastrado")
else:
    for indice, valor in enumerate(ddd):
        if ddd[indice]["ddd"] == value:
            print(ddd[indice]["Destination"])
    



