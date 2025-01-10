# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('Suas opções:')
print('[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Escolha uma opção: '))
computador = randint(0, 2)
escolha = ('pedra', 'papel', 'tesoura')

if jogador >= 0 and jogador <= 2:
   sleep(0.5)
   print('Jo')
   sleep(0.5)
   print('ken')
   sleep(0.5)
   print('pô')
   print(f'Computador jogou {escolha[computador]}.')
   print(f'Jogador jogou {escolha[jogador]}.')
   if jogador == computador:
      print('Houve empate.')
   elif (jogador == 0 and computador == 1) or (jogador == 2 and computador == 0):
      print('Computador venceu!')
   elif (jogador == 1 and computador == 0) or (jogador == 0 and computador == 2):
      print('Jogador venceu!')
else:
   print('Opção inválida. Tente novamente!')