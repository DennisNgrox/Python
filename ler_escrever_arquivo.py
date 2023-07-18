arquivo = open("arquivo.txt")

print(arquivo.read())
arquivo.close()

# or melhor:
# Forma utilizada normalmente:

with open("arquivo.txt") as arquivo:
    print(arquivo.read())

with open("arquivo.txt", "w") as arquivo: # Escrever uma string --- com w o conteúdo será substituido
    arquivo.write('Dennis, \n')

with open("arquivo.txt", "a") as arquivo: # adicionar uma string sem sobrescrever
    arquivo.write('Dennis, \n')
