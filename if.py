def defineIdade(idade):
    if idade < 18:
        return f'Menor de idade, você tem {idade} e para entrar precisa ter pelo menos 18 anos'
    else:
        return f'Pode entrar'
    

print(defineIdade(18))
print(defineIdade(17))