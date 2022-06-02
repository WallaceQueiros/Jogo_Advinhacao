import Advinhacao
import forca
print(32 * '*')
print('{:^32}'.format('Escolha seu Jogo!'))
print(32 * '*')

print('(1)-Advinhação / (2)-Forca')
opcao = int(input('Escolha 1 ou 2: '))
if opcao == 1:
    Advinhacao.jogar()
    print('Jogando Advinhação')
    opcao = 'Advinhação'
elif opcao == 2:
    forca.jogar()
    print('Jogando Forca')
    opcao = 'Forca'
