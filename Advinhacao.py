print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')
cont = 0
number_secret = 42
while True:

    chute = int(input('Digite o seu número: '))
    cont += 1
    print(f'Você já tentou {cont} vezes')
    print(f'Você digitou {chute}')

    if number_secret == chute:
        print('PARABÉNS, VOCÊ ACERTOU!')
        break
    else:
        if chute > number_secret:
            print('O número digitado é maior que o secreto')
        elif chute < number_secret:
            print('O número digitado é menor que o secreto')
        print('QUE PENA, VOCÊ ERROU!')
