lista = ['cookie','milk shake', 'danone','granola','peixe']

for i in lista:
    if i == 'peixe':
        print('Eu poderia comer peixe todos os dias! ')
    elif i == 'cookie':
        print('cookie é um alimento estranho')
    else:
        print(f'{i}, eu não gosto tanto assim ')



## while

comida_favorita = 'peixe'

comida = input('digite meu tipo de comida favorito ')
while comida != comida_favorita:
    print(f'ERROU! {comida} não é minha comida favorita! ')
    print('Tente novamente ')
    comida = input('digite meu tipo de comida favorito ')

print('Exatamente!! Peixe é minha comida favorita! ')



