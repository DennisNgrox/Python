a, b = input().split()
a = int(a)
b = int(b)

dic = [{
    "cod": 1,
    "especificacao": "cachorro quente",
    "valor": 4.00
    },
    {
    "cod": 2,
    "especificacao": "X-SALADA",
    "valor": 4.50
    },
    {
    "cod": 3,
    "especificacao": "X-BACON",
    "valor": 5.00
    },
    {
    "cod": 4,
    "especificacao": "Torrada",
    "valor": 2.00
    },
    {
    "cod": 5,
    "especificacao": "Refrigerante",
    "valor": 1.50
    }
]


for i, h in enumerate(dic):
    value = h["cod"]
    if value == a:
        valor = float(h["valor"])
        result = valor * b



print(f'Total: R$ {result:.2f}')

    
