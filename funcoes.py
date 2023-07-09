def mensagem(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

mensagem('Sistema de Professores')
mensagem('Sistema de Alunos')
mensagem('Sistem de Arquivos')

def contador (* núm):
    print(núm)


contador(1, 2, 3, 4)

# Pos começa em 0 (Posisão inicial da lista), enquanto a posição for menor
# que o tamanho total da lista (lst), cada posição será multipicado por 2
def soma(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 4, 6, 8, 20]
soma(valores)
print(valores)




