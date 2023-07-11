def voto(a):
    from datetime import date
    idade = date.today().year - a 
    if idade >= 18:
        return f'Com {idade} anos Seu voto é obrigatório'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos Seu voto é opcional'
    else:
        return f'Com {idade} anos Não pode Votar'

    
print(voto(int(input('Digite seu ano de nascimento: '))))
