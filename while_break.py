n = s = 0
while n != 999:
    n = int(input('Digite um valor '))
    if n == 999:
        break
    s += n


print(f'O resultado: {s}')
