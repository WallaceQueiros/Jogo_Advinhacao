from random import randint

print(32 * '*')
print('Bem vindo ao jogo de Adivinhação')
print(32 * '*')

tentativas = 0
number_secret = randint(0, 100)

while True:
    chute = int(input('Digite o seu número: '))
    print(32 * '=')
    tentativas += 1
    print(f'Você já tentou {tentativas} vezes')
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
