import moeda

p = float(input('Digite um valor: '))

print(f'Aumentando 10% de {p}, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10% de {p}, temos R${moeda.diminuir(p, 10)}')
print(f'O Dobro de {p}, temos R${moeda.dobro(p)}')
print(F'A metade de {p}, temos R${moeda.metade(p)}')

