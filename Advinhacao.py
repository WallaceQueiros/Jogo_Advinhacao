from random import randint

print(32 * '*')
print('Bem vindo ao jogo de Adivinhação')
print(32 * '*')

tentativas = 0
number_secret = randint(0, 100)

print('Escolha seu nível de dificuldade')
print('''(1) Facil 
(2) Médio 
(3) Difiil ''')

escolha = int(input('Nivel: '))
if escolha != 1 or escolha != 2 or escolha != 3:
    print('Escolha uma opção valida')
    escolha = int(input('Nivel: '))
print(32 * '*')

if escolha == 1:
    tentativas = 15
    escolha = 'Facil'

elif escolha == 2:
    tentativas = 8
    escolha = 'Médio'

elif escolha == 3:
    tentativas = 5
    escolha = 'Dificil'

print(f'Você escolheu o nivel {escolha.upper()} ')
print(49 * '=')

while True:
    print(f'Seu número de tentativas atual é: {tentativas}')
    chute = int(input('Digite o seu número: '))
    tentativas -= 1
    print(f'Você digitou: {chute}')
    if number_secret == chute:
        if escolha == 'Facil':
            tentativas *= 1
        if escolha == 'Médio':
            tentativas *= 5
        if escolha == 'Dificil':
            tentativas *= 10
        print('PARABÉNS, VOCÊ ACERTOU!')
        break
    elif tentativas == 0:
        print('VOCÊ PERDEU! ')
        break
    else:
        if chute > number_secret:
            print('O número digitado é maior que o secreto')
        elif chute < number_secret:
            print('O número digitado é menor que o secreto')
        print(32 * '=')
print(f'Sua pontuação final no nivel {escolha} foi de: {tentativas} pontos ')
