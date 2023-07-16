lista = [1, 2, 3, 4]

res = (item < 0 for item in lista)

print(res)

#Generator object -- necessario transformar em lista para ver resultado --- list(item < 0 for item in lista)
