print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')

number_secret = 42

chute = int(input('Digite o seu número: '))

print(f'Você digitou {chute}')

if number_secret == chute:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print('QUE PENA, VOCÊ ERROU!')
