from datetime import date

def voto(a):
    idade = date.today().year - a 
    return idade

    
PessoaIdade = voto(int(input('Qual seu ano de nascimento: ')))
if PessoaIdade >= 18:
    print(f'Com {PessoaIdade} anos Seu voto é obrigatório')
elif PessoaIdade >= 16 and PessoaIdade < 18:
    print(f'Com {PessoaIdade} anos Seu voto é opcional')
else:
    print(f'Com {PessoaIdade} anos Não pode Votar')
