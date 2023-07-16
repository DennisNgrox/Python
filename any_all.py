lista = [1, 2, 3, -1, -2, -3]

verifica_lista = [item > 0 for item in lista]

print(verifica_lista)

if any(verifica_lista):
    print(f'acima de 0')
else:
    print(f'abaixo de 0')


#any verifica se pelo menos um valor é true or false
#all verifica se todos valores são true ou false
